from odoo import fields, models


class PurchaseRequestLine(models.Model):
    _inherit = "purchase.request.line"

    availability_line_ids = fields.One2many(
        comodel_name="purchase.request.availability.line",
        inverse_name="request_line_id",
        string="Availability in other Stock Locations",
    )

    hide_request_line = fields.Boolean(default=False, copy=False, store=True)
