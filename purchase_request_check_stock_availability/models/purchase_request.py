from odoo import fields, models


class PurchaseRequest(models.Model):
    # 1. Private attributes
    _inherit = "purchase.request"

    # 2. Fields declaration
    availability_line_ids = fields.One2many(
        comodel_name="purchase.request.availability.line",
        inverse_name="request_id",
        string="Available Products",
    )

    stock_picking_ids = fields.One2many(
        comodel_name="stock.picking",
        inverse_name="purchase_request_id",
        string="Internal Transfers",
    )

    line_ids = fields.One2many(domain=[("hide_request_line", "!=", True)])

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    def check_stock_availability(self):
        stock_location_model = self.env["stock.location"]
        availability_line_model = self.env["purchase.request.availability.line"]

        # Clear current lines
        self.availability_line_ids = False

        # Get all locations where to search for the products
        args = self.get_stock_location_domain()
        locations_to_check = stock_location_model.search(args)

        # Consumables can be removed with this option
        remove_consumables = self.company_id.check_availability_remove_consumable

        # Iterate all lines on the PR, check their available quantities in
        # different stock locations, and create availability lines accordingly
        for request_line in self.line_ids:
            # A request line is removed and a comment is added to purchase request if
            # removing consumables has been actived from settings and a product is of
            # consumable type
            if remove_consumables and request_line.product_id.detailed_type == "consu":
                display_msg = """<div style="color: green;">
                    Note by: {}
                    </div>
                    <div style="color: green;">
                    {}
                    </div>
                    <div style="color: green;">
                    A request line with the product {}
                    and quantity of {}
                    has been removed after 'Check Other Locations' Availability' was used.
                    </div>
                    """.format(
                    self.env.user.partner_id.name,
                    "_" * (len("Note by:") + len(self.env.user.partner_id.name)),
                    request_line.product_id.display_name,
                    request_line.product_qty,
                )

                self.message_post(
                    message_type="comment",
                    subject="Request line removed",
                    body=display_msg,
                    body_is_html=True,
                    author_id=self.env.user.partner_id.id,
                )

                request_line.unlink()
                continue

            for location in locations_to_check:
                qty_available = request_line.product_id.with_context(
                    location=location.id
                ).qty_available

                if qty_available > 0:
                    availability_line_model.create(
                        {
                            "request_id": self.id,
                            "request_line_id": request_line.id,
                            "available_qty": qty_available,
                            "location_id": location.id,
                        }
                    )

    # 8. Business methods
    def get_stock_location_domain(self):
        """What stock locations should be included when checking if materials
        exist elsewhere. By default included ones are internal physical
        locations that are linked to an analytic account (i.e. are project
        locations) and belong to the same company. The location set on the
        purchase request is filtered out to avoid suggesting same source/target
        locations
        """

        search_domain = [
            ("company_id", "=", self.company_id.id),
            ("id", "!=", self.stock_location_id.id),
            ("usage", "=", "internal"),
            ("analytic_account_id", "!=", False),
        ]

        search_with_excess = self.company_id.check_availability_with_excess

        if search_with_excess:
            search_domain += [("is_excess_location", "=", True)]

        return search_domain
