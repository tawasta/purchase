from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    date_receipt_requested = fields.Datetime(
        string="Requested Receipt Date",
        help="Delivery date requested from the supplier",
    )
