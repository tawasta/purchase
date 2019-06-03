# -*- coding: utf-8 -*-


from odoo import fields, models
from odoo.addons.purchase.models.purchase import PurchaseOrder as purchase_o


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    user_id = fields.Many2one(
        'res.users',
        string='Buyer',
        states=purchase_o.READONLY_STATES
    )
