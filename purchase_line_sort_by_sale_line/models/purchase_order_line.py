from odoo import api, fields, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"
    _order = (
        "linked_sale_line_sequence, linked_sale_line_id_number, order_id, sequence, id"
    )

    linked_sale_line_id_number = fields.Integer(
        string="Linked sale id number", compute="_compute_linked_sale_line", store=True
    )
    linked_sale_line_sequence = fields.Integer(
        string="Linked sale sequence", compute="_compute_linked_sale_line", store=True
    )

    @api.depends("move_dest_ids")
    def _compute_linked_sale_line(self):
        for line in self:
            if line.order_id.state == "draft":
                sale_lines = (
                    line.move_dest_ids
                    and [x.sale_line_id for x in line.move_dest_ids]
                    or False
                )
            else:
                moves = line.move_ids and line.move_ids[0]
                sale_lines = (
                    moves and [x.sale_line_id for x in moves.move_dest_ids] or False
                )
            if sale_lines:
                line.linked_sale_line_id_number = abs(1 - sale_lines[0].id)
                line.linked_sale_line_sequence = sale_lines[0].sequence
            else:
                line.linked_sale_line_id_number = False
                line.linked_sale_line_sequence = False
