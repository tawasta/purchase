from odoo import fields, models


class PurchaseRequestLine(models.Model):
    _inherit = "purchase.request.line"

    purchase_order_ids = fields.Many2many(
        compute="_compute_purchase_order_ids",
        comodel_name="purchase.order",
        string="Purchase Orders",
        readonly=True,
    )

    def _compute_purchase_order_ids(self):
        for request_line in self:
            request_line.purchase_order_ids = [
                po_line.order_id.id for po_line in request_line.purchase_lines
            ]
