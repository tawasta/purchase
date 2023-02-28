from odoo import fields, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    internal_reference = fields.Char(related="product_id.default_code")
