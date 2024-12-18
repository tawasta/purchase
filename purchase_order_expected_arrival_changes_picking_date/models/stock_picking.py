from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    po_date_planned = fields.Datetime(
        string="Purchase Expected Arrival", store=True, copy=False
    )

    @api.depends("move_ids.state", "move_ids.date", "move_type")
    def _compute_scheduled_date(self):
        res = super()._compute_scheduled_date()

        for picking in self:
            if picking.po_date_planned:
                picking.scheduled_date = picking.po_date_planned
        return res
