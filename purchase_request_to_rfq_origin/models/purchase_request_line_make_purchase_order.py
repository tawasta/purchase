# -*- coding: utf-8 -*-


from odoo import api, models


class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):

    _inherit = 'purchase.request.line.make.purchase.order'

    @api.model
    def _prepare_purchase_order(self, picking_type, location, company):

        res = super(PurchaseRequestLineMakePurchaseOrder, self).\
            _prepare_purchase_order(picking_type, location, company)

        if res.get('origin') is not False:
            res['origin'] = self.item_ids.request_id.name

        return res
