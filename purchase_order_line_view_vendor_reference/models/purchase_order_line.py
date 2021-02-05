from odoo import api, fields, models


class PurchaseOrderLine(models.Model):

    _inherit = 'purchase.order.line'

    partner_ref = fields.Char(related="order_id.partner_ref")
