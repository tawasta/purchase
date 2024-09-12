from odoo import api, fields, models
import datetime


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.depends("order_line.date_planned", "order_line")
    def _compute_latest_effective_date(self):
        for purchase in self:
            # A convention
            latest_date = datetime.datetime(1970, 1, 1)

            for line in purchase.order_line:
                if line.date_planned > latest_date:
                    latest_date = line.date_planned

            purchase.latest_effective_date = latest_date

    latest_effective_date = fields.Datetime(
        string="Latest Expected Arrival",
        compute="_compute_latest_effective_date",
        store=True,
        copy=False,
        help="Computed from lines' expected arrival dates",
    )
