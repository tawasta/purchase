from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    always_show_hs_code = fields.Boolean(
        string="Always show HS code on print",
        related="company_id.always_show_hs_code",
        readonly=False,
    )
