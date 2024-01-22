from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    purchase_order_standard_clause = fields.Text(
        related="company_id.purchase_order_standard_clause",
        translate=True,
        readonly=False,
    )
