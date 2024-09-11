from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    show_purchase_header = fields.Boolean(
        "Show header on report",
        config_parameter="purchase.show_purchase_header",
        help="Show header value on Purchase Report.",
    )
