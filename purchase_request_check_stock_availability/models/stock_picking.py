from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    purchase_request_id = fields.Many2one(
        comodel_name="purchase.request", string="Purchase Request"
    )

    purchase_request_line_id = fields.Many2one(
        comodel_name="purchase.request.line", string="Purchase Request Line"
    )

    def button_validate(self):
        for picking in self:
            picking.purchase_request_line_id.unlink()
        return super().button_validate()

    def unlink(self):
        for picking in self:
            picking.purchase_request_line_id.hide_request_line = False
        return super().unlink()
