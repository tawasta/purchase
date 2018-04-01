# -*- coding: utf-8 -*-
from odoo import models, fields


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    date_receipt_requested = fields.Datetime(
        string='Requested Receipt Date',
        readonly=True,
        states={
            'draft': [('readonly', False)],
            'sent': [('readonly', False)],
            'to_approve': [('readonly', False)]
        },
        help='Delivery date requested from the supplier'
    )
