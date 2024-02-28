from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.onchange("product_id")
    def onchange_product_id(self):
        res = super().onchange_product_id()

        project_id = self.order_id and self.order_id.project_id

        if project_id:
            distr = dict()
            distr[project_id.id] = 100

            self.analytic_distribution = distr
        return res
