from odoo import api, models


class PrLineMakePo(models.TransientModel):

    _inherit = "purchase.request.line.make.purchase.order"

    @api.model
    def _prepare_purchase_order(self, picking_type, group_id, company, origin):

        purchase_order_model = self.env['purchase.order']
        res = super(PrLineMakePo, self)._prepare_purchase_order(picking_type,
                                                                group_id,
                                                                company,
                                                                origin)
        items = self.item_ids and self.item_ids[0]

        if hasattr(purchase_order_model, 'project_id') and items:
            res['project_id'] = items.request_id.analytic_account_id.id

        return res
