# -*- coding: utf-8 -*-


from odoo import models, fields
from odoo.addons.purchase.models.purchase import PurchaseOrder as purchase_o


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    def _get_buyer_id(self):
        return self.env.uid

    user_id = fields.Many2one(
        default=_get_buyer_id,
        comodel_name='res.users',
        string="Buyer",
        states=purchase_o.READONLY_STATES
    )
