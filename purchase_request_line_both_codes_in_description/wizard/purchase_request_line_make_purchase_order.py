# -*- coding: utf-8 -*-

from odoo import api, models


class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):

    _inherit = "purchase.request.line.make.purchase.order"

    @api.model
    def _prepare_purchase_order_line(self, po, item):
        # Force default code and vendor code to purchase order line description

        res = super(PurchaseRequestLineMakePurchaseOrder,
                    self)._prepare_purchase_order_line(po, item)

        product = item.product_id.with_context(
            replace_supplier_code=True,
            partner_id=po.partner_id.id,
        )
        res['name'] = product.display_name

        return res
