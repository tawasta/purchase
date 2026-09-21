from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    print_manuf_code = fields.Boolean(
        string="Print Manufacturer Code",
        default=False,
    )
