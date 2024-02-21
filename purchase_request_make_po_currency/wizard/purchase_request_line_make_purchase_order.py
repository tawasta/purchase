from odoo import api, models


class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):
    _inherit = "purchase.request.line.make.purchase.order"

    @api.model
    def _prepare_purchase_order(self, picking_type, group_id, company, origin):
        data = super()._prepare_purchase_order(picking_type, group_id, company, origin)
        supplier = self.supplier_id
        if supplier.property_purchase_currency_id:
            data["currency_id"] = supplier.property_purchase_currency_id.id
        return data
