from odoo import fields, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    hs_code_id = fields.Many2one("hs.code", related="product_id.hs_code_id")
