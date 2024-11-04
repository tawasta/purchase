from odoo import models
import logging

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def print_purchase_order(self):
        return self.env.ref("purchase.action_report_purchase_order").report_action(
            self.id
        )
