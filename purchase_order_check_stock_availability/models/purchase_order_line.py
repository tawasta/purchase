from odoo import fields, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    availability_line_ids = fields.One2many(
        comodel_name="purchase.order.availability.line",
        inverse_name="order_line_id",
        string="Availability in other Stock Locations",
    )
