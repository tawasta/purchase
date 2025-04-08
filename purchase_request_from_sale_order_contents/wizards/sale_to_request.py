from odoo import models, fields


class SaleToRequest(models.TransientModel):
    _name = "purchase_request_from_sale_contents.sale_to_request"
    _description = "Import Sale Order contents to purchase request"
    _rec_name = "sale_id"

    def calculate_quantities(self):
        for line in self.sale_id.order_line:
            self.env["purchase_request_from_sale_contents.sale_to_request_line"].create(
                {
                    "product_id": line.product_id.id,
                    "uom_id": line.product_id.uom_id.id,
                    "qty": line.product_uom_qty,
                    "wizard_id": self.id,
                }
            )

        # Reopen the wizard after state change
        self.state = "qty_calculation"
        return {
            "context": self.env.context,
            "view_type": "form",
            "view_mode": "form",
            "res_model": "purchase_request_from_sale_contents.sale_to_request",
            "res_id": self.id,
            "type": "ir.actions.act_window",
            "target": "new",
            "name": "Sale Order To Purchase Request",
        }

    def get_request_line_values(self, line, purchase_request_id):
        # Override to provide extra values
        return {
            "product_id": line.product_id.id,
            "request_id": purchase_request_id,
        }

    def get_line_domain(self, line, purchase_request_id):
        return [
            ("product_id", "=", line.product_id.id),
            ("product_uom_id", "=", line.uom_id.id),
            ("request_id", "=", purchase_request_id),
        ]

    def add_request_lines(self):
        purchase_request_line_model = self.env["purchase.request.line"]
        purchase_request_id = self._context["active_id"]

        for line in self.product_line_ids:
            domain = self.get_line_domain(line, purchase_request_id)

            matching_request_line = purchase_request_line_model.search(domain, limit=1)

            if self.combine_with_existing and matching_request_line:
                matching_request_line[0].product_qty = matching_request_line[
                    0
                ].product_qty + (line.qty * self.multiplier)
            else:
                pr_line_values = self.get_request_line_values(line, purchase_request_id)

                res = purchase_request_line_model.create(pr_line_values)
                # Call onchange to get the full product description,
                # and add rest of the line info afterwards
                res.onchange_product_id()
                res.write(
                    {
                        "product_uom_id": line.uom_id.id,
                        "product_qty": line.qty * self.multiplier,
                    }
                )

    sale_id = fields.Many2one(comodel_name="sale.order", string="Sale Order")

    product_line_ids = fields.One2many(
        comodel_name="purchase_request_from_sale_contents.sale_to_request_line",
        inverse_name="wizard_id",
        string="Components",
    )

    state = fields.Selection(
        selection=[
            ("sale_selection", "Sale order Selection"),
            ("qty_calculation", "Quantity Calculation"),
        ],
        default="sale_selection",
    )

    multiplier = fields.Integer(
        string="Multiplier",
        default=1,
        help=(
            """Change this to e.g. 5 if you want to add 5 sale orders worth
              of components to the purchase request"""
        ),
    )

    combine_with_existing = fields.Boolean(
        string="Combine with existing Purchase Request lines",
        default=True,
        help=(
            """If the same product already exists on the Purchase Request,
              the quantities are merged."""
        ),
    )
