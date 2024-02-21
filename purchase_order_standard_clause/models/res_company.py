from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    purchase_order_standard_clause = fields.Text(
        string="Purchase Order Standard Clause",
        help="Suggested as a default for new Purchase Orders",
        translate=True,
    )
