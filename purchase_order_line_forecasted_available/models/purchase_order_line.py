from odoo import fields, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    virtual_available = fields.Float(
        "Forecast Quantity",
        related="product_id.product_tmpl_id.virtual_available",
        readonly=True,
        store=True,
    )
