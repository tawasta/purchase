# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    reference = fields.Char('Internal Reference')