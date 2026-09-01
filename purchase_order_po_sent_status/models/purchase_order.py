from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[("po_sent", "PO Sent"), ("to approve",)])

    def print_purchase_order(self):
        self.write({"state": "po_sent"})
        return self.env.ref("purchase.action_report_purchase_order").report_action(
            self.id
        )

    def _track_subtype(self, init_values):
        subtypes = super()._track_subtype(init_values=init_values)

        if "state" in init_values and self.state == "po_sent":
            return self.env.ref("purchase_order_po_sent_status.mt_po_sent")
        return subtypes
