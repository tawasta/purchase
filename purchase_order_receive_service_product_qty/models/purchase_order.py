from odoo import api, models


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.multi
    def button_confirm(self):
        result = super().button_confirm()

        # Search for lines which have service as their product type
        lines = (x for x in self.order_line if x.product_id.type == 'service')

        for line in lines:
            # Set received qty the same as ordered qty
            line.qty_received = line.product_qty

        return result
