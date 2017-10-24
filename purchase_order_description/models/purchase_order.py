# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class PurchaseOrder(models.Model):
    
    _inherit = 'purchase.order'

    description = fields.Text('Description',
                              help='Internal notes')
