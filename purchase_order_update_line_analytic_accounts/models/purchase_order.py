# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.one
    def set_line_analytic(self):
        if not self.value_set_line_analytic:
            raise exceptions.UserError(_('Please select an Analytic Account first'))
        for line in self.order_line:
            line.account_analytic_id = self.value_set_line_analytic.id
        self.value_set_line_analytic = False

    # Dummy field for selecting the AA to set. Always gets cleared after setting
    value_set_line_analytic = fields.Many2one('account.analytic.account', 'Analytic Account for PO lines')
    
