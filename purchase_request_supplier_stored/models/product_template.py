# -*- coding: utf-8 -*-
from odoo import api, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    @api.multi
    @api.depends('seller_ids')
    def _compute_purchase_request_line_suppliers(self):
        purchase_request_line = self.env['purchase.request.line']

        for record in self:
            request_lines = purchase_request_line.search([
                ('product_id', '=', record.product_variant_ids.ids),
            ])
            request_lines._compute_supplier_id()
