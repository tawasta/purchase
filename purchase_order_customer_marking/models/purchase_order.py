from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    customer_marking = fields.Char(copy=False)
