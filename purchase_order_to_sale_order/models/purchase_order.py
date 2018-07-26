# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one(
        string='Related sale',
        comodel_name='sale.order',
        copy=False,
    )

    def action_create_sale_order(self):
        self.ensure_one()

        if self.sale_order_id:
            raise UserError(_('A sale order already exists'))

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_origin': self.name,
                'default_purchase_order_ids': [(6, 0, [self.id])],
            },
        }
