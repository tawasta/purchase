# -*- coding: utf-8 -*-
from odoo import api, models


class PurchaseOrderLine(models.Model):

    _inherit = 'purchase.order.line'

    @api.onchange('account_analytic_id')
    def onchange_account_analytic_id_update_analytic_tags(self):
        for record in self:
            if record.account_analytic_id and \
                    record.account_analytic_id.tag_ids:

                record.analytic_tag_ids += record.account_analytic_id.tag_ids

    @api.onchange('project_id')
    def onchange_project_id_update_analytic_tags(self):
        for record in self:
            if record.project_id and \
                    record.project_id.tag_ids:

                record.analytic_tag_ids += record.project_id.tag_ids
