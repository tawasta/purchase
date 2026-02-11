from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    purchase_report_decimal_precision = fields.Integer(
        related="company_id.purchase_report_decimal_precision",
        readonly=False,
        store=True,
    )
