
from odoo import api, models


class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):

    _inherit = 'purchase.request.line.make.purchase.order'

    @api.model
    def _prepare_purchase_order(self, picking_type, group_id, company, origin):
        data = super()._prepare_purchase_order(picking_type, group_id, company, origin)
        supplier = self.supplier_id
        # Assign Payment Terms from vendor
        if supplier.property_supplier_payment_term_id:
            data['payment_term_id'] = supplier.property_supplier_payment_term_id.id
        # Assign Additional Terms from vendor
        if supplier.additional_term_id:
            data['additional_term_id'] = supplier.additional_term_id.id
        return data
