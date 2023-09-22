from odoo import api, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    @api.onchange("product_id")
    def onchange_product_id_update_analytic_tags(self):
        if self.product_id:
            self.analytic_tag_ids += self.product_id.get_analytic_tags()
