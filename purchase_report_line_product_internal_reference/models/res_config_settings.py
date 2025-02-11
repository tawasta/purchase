from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    purchase_report_line_internal_reference_position = fields.Selection(
        related="company_id.purchase_report_line_internal_reference_position",
        readonly=False,
    )
