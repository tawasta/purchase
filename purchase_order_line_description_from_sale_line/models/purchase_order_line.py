from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = "plain.model"

    @api.model_create_multi
    def create(self, vals_list):
        for values in vals_list:
            moves = values.get("move_dest_ids", False)
            move_id = moves and isinstance(moves[0], tuple) and moves[0][1] or False
            stock_move = move_id and self.env["stock.move"].browse(move_id) or False
            sale_line = stock_move and stock_move.sale_line_id or False

            if sale_line:
                values["name"] = sale_line.name
        return super().create(vals_list)
