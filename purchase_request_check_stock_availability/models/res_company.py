from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    check_availability_with_excess = fields.Boolean(
        string="Check Availability for Excess locations",
        help=(
            "Use this option to check availability for excess locations "
            "on purchase request."
        ),
    )
