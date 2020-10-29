from odoo import api, fields, models, exceptions, _
import odoo.addons.decimal_precision as dp


class PurchaseOrderAvailabilityLine(models.Model):

    _name = "purchase.order.availability.line"
    _description = "Purchase Order Availability Line"
    _order = "order_id, product_id"
    _rec_name = "order_line_id"

    order_line_id = fields.Many2one(
        comodel_name="purchase.order.line", string="Related Order Line",
    )
    product_id = fields.Many2one(
        related="order_line_id.product_id",
        comodel_name="product.product",
        string="Product",
    )

    product_qty = fields.Float(
        related="order_line_id.product_qty",
        string="Quantity wanted",
        digits=dp.get_precision("Product Unit of Measure"),
    )

    analytic_account_id = fields.Many2one(
        related="order_line_id.account_analytic_id",
        comodel_name="account.analytic.account",
        string="Analytic Account",
    )

    product_uom_id = fields.Many2one(
        related="order_line_id.product_uom", comodel_name="uom.uom", string="UoM"
    )

    available_qty = fields.Float(
        string="Quantity at location",
        digits=dp.get_precision("Product Unit of Measure"),
    )

    available_uom_id = fields.Many2one(
        related="order_line_id.product_id.uom_id", comodel_name="uom.uom", string="UoM"
    )

    order_id = fields.Many2one(comodel_name="purchase.order", string="Purchase Order",)

    location_id = fields.Many2one(comodel_name="stock.location", string="Location")

    location_dest_id = fields.Many2one(
        comodel_name="stock.location",
        string="Destination",
        related="order_line_id.location_dest_id",
    )

    company_id = fields.Many2one(
        related="order_id.company_id", comodel_name="res.company", string="Company"
    )

    active = fields.Boolean(default=True, string="Active")

    @api.multi
    def create_transfer(self):
        """ Creates a new stock picking for transfering raw materials
        to the location defined in the PR """
        self.ensure_one()

        if not self.location_id or not self.location_dest_id:
            raise exceptions.UserError(
                _("Please set source and destination location first")
            )

        stock_picking_model = self.env["stock.picking"]
        stock_move_model = self.env["stock.move"]

        vals = {
            "purchase_id": self.order_id.id,
            "picking_type_id": self._get_picking_type_for_transfer(),
            "location_id": self.location_id.id,
            "location_dest_id": self.location_dest_id.id,
            "origin": "%s: %s %s"
            % (self.order_id.name, _("Internal transfer of"), self.product_id.name),
        }

        res = stock_picking_model.create(vals)

        # TODO: UOM handling when using different units of measure
        transfer_qty = self._get_transfer_qty()

        stock_move_model.create(
            {
                "name": self.product_id.name,
                "picking_id": res.id,
                "purchase_line_id": self.order_line_id.id,
                "product_id": self.product_id.id,
                "product_uom": self.product_uom_id.id,
                "product_uom_qty": transfer_qty,
                "location_id": res.location_id.id,
                "location_dest_id": res.location_dest_id.id,
            }
        )

        if self.product_qty <= transfer_qty:
            # The whole qty is expected to be transferred, so remove all
            # availability lines related to the order line. We cannot
            # completely delete the lines yet to avoid "Record does not exist
            # or has been deleted" error, so mark them as inactive instead
            for line in self.order_line_id.availability_line_ids:
                line.active = False
            # Delete the actual purchase order line
            # self.order_line_id.unlink()
            self.order_line_id.product_qty -= transfer_qty
        else:
            # If only a part of the whole qty is expected to be transferred,
            # subtract the transfer amount from the purchase order line
            self.order_line_id.product_qty -= transfer_qty

        return {
            "name": "%s / Internal transfers" % self.order_id.name,
            "view_type": "form",
            "view_mode": "form, tree",
            "res_model": "stock.picking",
            "type": "ir.actions.act_window",
            "target": "current",
            "res_id": res.id,
        }

    def _get_picking_type_for_transfer(self):
        """ What picking type should be used for the new stock picking.
        Default is an internal tranfer for the company of the purchase
        orders"""
        args = [
            ("code", "=", "internal"),
            ("warehouse_id.company_id", "=", self.order_id.company_id.id),
        ]

        res = self.env["stock.picking.type"].search(args, limit=1)

        if not res:
            raise exceptions.UserError(_("Stock picking type not found!"))
        else:
            return res[0].id

    def _get_transfer_qty(self):
        """How much of the product should be suggested to be transferred
        on the picking. Default is:
        -Total order quantity if available
        -If total amount is not available, then transfer as much as possible"""
        return min(self.available_qty, self.product_qty)
