# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, exceptions


class ResCompany(models.Model):

    _inherit = 'res.company'

    purchase_order_standard_clause = fields.Text(
        string='Purchase Order Standard Clause',
        help='''Suggested as a default for new Purchase Orders''',
        translate=True)