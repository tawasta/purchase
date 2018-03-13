# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.tools.translate import _


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    supplier_contact_id = fields.Many2one('res.partner', "Vendor's contact")
