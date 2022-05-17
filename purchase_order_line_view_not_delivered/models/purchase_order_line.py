from odoo import api, fields, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    qty_not_delivered = fields.Float(
        "Not Delivered",
        help="Quantity of items not yet delivered (Ordered minus delivered).",
        compute="_compute_qty_not_delivered",
    )

    @api.depends("product_qty", "qty_received")
    def _compute_qty_not_delivered(self):
        for pol in self:
            pol.qty_not_delivered = pol.product_qty - pol.qty_received
