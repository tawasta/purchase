from odoo import api, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    @api.onchange("account_analytic_id")
    def onchange_account_analytic_id_update_analytic_tags(self):
        if self.account_analytic_id and self.account_analytic_id.tag_ids:
            self.analytic_tag_ids += self.account_analytic_id.tag_ids
