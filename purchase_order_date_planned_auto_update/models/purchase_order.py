# -*- coding: utf-8 -*-
from odoo import models, api


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.onchange('date_planned')
    def onchange_date_planned_update_lines(self):
        for record in self:
            record.action_set_date_planned()
