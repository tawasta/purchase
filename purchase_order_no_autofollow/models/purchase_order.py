from odoo import models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    def button_confirm(self):
        res = super().button_confirm()
        for order in self:
            # We can't prevent the subscription, so we'll just
            # unsubscribe right after the confirmation
            if order.partner_id in order.message_partner_ids:
                order.message_unsubscribe([order.partner_id.id])
        return res
