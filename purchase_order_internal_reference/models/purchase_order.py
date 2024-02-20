from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    reference = fields.Char(string="Internal Reference")
