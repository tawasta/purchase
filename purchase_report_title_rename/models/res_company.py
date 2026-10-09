from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    purchase_order_report_title = fields.Char(
        default="",
        translate=True,
    )
    purchase_rfq_report_title = fields.Char(
        string="RFQ Report Title",
        default="",
        translate=True,
    )
