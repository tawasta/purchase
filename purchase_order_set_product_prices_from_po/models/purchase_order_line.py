# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class PurchaseOrderLine(models.Model):
    
    _inherit = 'purchase.order.line'

    update_price = fields.Boolean('Update Cost Price', help='''Checked lines' products will have their Cost Prices updated according to the price on the line when Purchase Order's 'Update Prices' button is clicked. ''')