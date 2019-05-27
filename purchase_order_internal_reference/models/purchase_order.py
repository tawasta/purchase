from odoo import models, fields


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    reference = fields.Char(
        string='Internal Reference'
    )
