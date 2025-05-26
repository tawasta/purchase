from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    purchase_order_standard_clause = fields.Text(
        help="Suggested as a default for new Purchase Orders",
        translate=True,
    )
