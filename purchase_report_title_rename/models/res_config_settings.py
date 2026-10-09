from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    purchase_order_report_title = fields.Char(
        string="Purchase Order Report Title",
        related="company_id.purchase_order_report_title",
        readonly=False,
        translate=True,
    )
    purchase_rfq_report_title = fields.Char(
        string="RFQ Report Title",
        related="company_id.purchase_rfq_report_title",
        readonly=False,
        translate=True,
    )
