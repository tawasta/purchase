# -*- coding: utf-8 -*-
from odoo import api, models, fields


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.multi
    def button_confirm(self):
        for order in self:
            order.date_confirmation = fields.Datetime.now()

        return super(PurchaseOrder, self).button_confirm()

    date_confirmation = fields.Datetime(
        string='Confirmation Date',
        readonly=True,
        help='Date when the Purchase Order was confirmed'
    )
