from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    check_availability_with_excess = fields.Boolean(
        related="company_id.check_availability_with_excess",
        readonly=False,
    )
