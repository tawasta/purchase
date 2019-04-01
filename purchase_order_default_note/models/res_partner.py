# -*- coding: utf-8 -*-

from openerp import fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    purchase_note = fields.Text(
        string='Purchase note',
        help='Default purchase note',
        )
