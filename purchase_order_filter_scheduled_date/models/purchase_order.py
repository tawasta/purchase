# -*- coding: utf-8 -*-


from odoo import api, fields, models


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.multi
    def _get_picking_state(self):
        for order in self:
            has_been_shipped = True

            for picking_id in order.picking_ids:
                for pick in picking_id:
                    has_been_shipped = has_been_shipped \
                        and pick.state == 'done'

            order.has_been_shipped = has_been_shipped

    @api.multi
    def _search_has_been_shipped(self, operator, value):
        recs = self.search([]).filtered(
            lambda x: x.has_been_shipped is False)
        if recs:
            return [('id', 'in', [x.id for x in recs])]

    has_been_shipped = fields.Boolean(
        string='Delivered',
        compute=_get_picking_state,
        search='_search_has_been_shipped'
        )
