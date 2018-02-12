# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, exceptions


class PurchaseConfigSettings(models.TransientModel):

    _inherit = 'purchase.config.settings'

    purchase_order_standard_clause = fields.Text(
        related='company_id.purchase_order_standard_clause',
        translate=True)