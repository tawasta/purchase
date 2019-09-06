# -*- coding: utf-8 -*-


from odoo import api, fields, models


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    tax_selection = fields.Many2many(
        comodel_name='account.tax',
        string='Taxes to assign',
    )

    @api.onchange('tax_selection')
    def assign_taxes(self):
        """Assign taxes for PO's lines"""
        self.ensure_one()
        for line in self.order_line:
            # The list of linked records are replaced with the
            # provided list using (6,_, [ids])
            line.taxes_id = [(6, 0, self.tax_selection.ids)]
