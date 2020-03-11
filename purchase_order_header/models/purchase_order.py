from odoo import fields, models


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    header_text = fields.Char(string='Header', help='Header or title of the Purchase')
