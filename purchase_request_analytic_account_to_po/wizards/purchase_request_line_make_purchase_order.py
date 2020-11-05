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

        # If the purchase order has a top-level analytic account field
        # (from e.g.) purchase_order_analytic_account, set it to contain
        # the purchase request's top-level analytic account
        if hasattr(purchase_order_model, 'project_id') \
                and self._context.get('active_id', None):
            res['project_id'] = self.env['purchase.request.line'] \
                .browse(self._context['active_id']) \
                .request_id.analytic_account_id.id

        return res
