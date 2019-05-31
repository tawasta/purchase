# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PurchaseRequestLine(models.Model):

    _inherit = 'purchase.request.line'

    supplier_id = fields.Many2one(
        store=True,
    )

    @api.multi
    @api.depends('product_id')
    def _compute_supplier_id(self):
        return super(PurchaseRequestLine, self)._compute_supplier_id()
