from odoo import _, exceptions, fields, models

import odoo.addons.decimal_precision as dp


class PurchaseRequestAvailabilityLine(models.Model):
    _name = "purchase.request.availability.line"
    _description = "Purchase Request Availability Line"
    _order = "request_id, request_line_id"
    _rec_name = "request_line_id"

    analytic_precision = fields.Integer(
        store=False,
        default=lambda self: self.env["decimal.precision"].precision_get(
            "Percentage Analytic"
        ),
    )

    request_line_id = fields.Many2one(
        comodel_name="purchase.request.line",
        string="Related Request Line",
    )

    product_id = fields.Many2one(
        related="request_line_id.product_id",
        comodel_name="product.product",
        string="Product",
    )

    product_qty = fields.Float(
        related="request_line_id.product_qty",
        string="Quantity wanted",
        digits=dp.get_precision("Product Unit of Measure"),
    )

    analytic_distribution_rel = fields.Json(
        related="request_line_id.analytic_distribution",
        string="Analytic Distribution",
    )

    product_uom_id = fields.Many2one(
        related="request_line_id.product_uom_id", comodel_name="uom.uom", string="UoM"
    )

    # This is the general available quantity
    qty_available = fields.Float(
        string="Quantity Available",
        digits=dp.get_precision("Product Unit of Measure"),
        related="product_id.qty_available",
    )

    available_qty = fields.Float(
        string="Quantity at location",
        digits=dp.get_precision("Product Unit of Measure"),
    )

    available_uom_id = fields.Many2one(
        related="request_line_id.product_id.uom_id",
        comodel_name="uom.uom",
        string="UoM",
    )

    request_id = fields.Many2one(
        comodel_name="purchase.request",
        string="Purchase Request",
    )

    location_id = fields.Many2one(comodel_name="stock.location", string="Location")

    company_id = fields.Many2one(
        related="request_id.company_id", comodel_name="res.company", string="Company"
    )

    active = fields.Boolean(default=True, string="Active")

    def create_transfer(self):
        """Creates a new stock picking for transfering raw materials
        to the location defined in the PR"""
        self.ensure_one()

        if not self.request_id.stock_location_id:
            raise exceptions.UserError(_("Please set the stock location first"))

        stock_picking_model = self.env["stock.picking"]
        stock_move_model = self.env["stock.move"]

        vals = {
            "purchase_request_id": self.request_id.id,
            "purchase_request_line_id": self.request_line_id.id,
            "picking_type_id": self._get_picking_type_for_transfer(),
            "location_id": self.location_id.id,
            "location_dest_id": self.request_id.stock_location_id.id or False,
            "origin": "%s: %s %s"
            % (self.request_id.name, _("Internal transfer of"), self.product_id.name),
        }

        res = stock_picking_model.create(vals)

        # TODO: UOM handling when using different units of measure
        transfer_qty = self._get_transfer_qty()

        stock_move_model.create(
            {
                "name": self.product_id.name,
                "picking_id": res.id,
                "product_id": self.product_id.id,
                "product_uom": self.product_uom_id.id,
                "product_uom_qty": transfer_qty,
                "location_id": res.location_id.id,
                "location_dest_id": res.location_dest_id.id,
            }
        )

        if self.product_qty <= transfer_qty:
            # The whole qty is expected to be transferred, so remove all
            # availability lines related to the request line. We cannot
            # completely delete the lines yet to avoid "Record does not exist
            # or has been deleted" error, so mark them as inactive instead
            for line in self.request_line_id.availability_line_ids:
                line.active = False
            # Hide the actual purchase request line before validating the related picking.
            # This line is deleted after picking has been validated.
            self.request_line_id.hide_request_line = True
        else:
            # If only a part of the whole qty is expected to be transferred,
            # subtract the transfer amount from the purchase request line
            self.request_line_id.product_qty -= transfer_qty

        return {
            "name": "%s / Internal transfers" % self.request_id.name,
            "view_type": "form",
            "view_mode": "form,tree",
            "res_model": "stock.picking",
            "type": "ir.actions.act_window",
            "target": "current",
            "res_id": res.id,
        }

    def _get_picking_type_for_transfer(self):
        """What picking type should be used for the new stock picking.
        Default is an internal tranfer for the company of the purchase
        request"""
        args = [
            ("code", "=", "internal"),
            ("warehouse_id.company_id", "=", self.request_id.company_id.id),
        ]

        res = self.env["stock.picking.type"].search(args, limit=1)

        if not res:
            raise exceptions.UserError(_("Stock picking type not found!"))
        else:
            return res[0].id

    def _get_transfer_qty(self):
        """How much of the product should be suggested to be transferred
        on the picking. Default is:
        -Total request quantity if available
        -If total amount is not available, then transfer as much as possible"""
        return min(self.available_qty, self.product_qty)
