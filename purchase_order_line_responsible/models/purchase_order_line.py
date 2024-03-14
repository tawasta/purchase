from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    responsible_id = fields.Many2one(related="product_id.responsible_id")
