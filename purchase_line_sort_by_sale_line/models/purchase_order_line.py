from odoo import api, fields, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    linked_sale_line_id_number = fields.Integer(
        string="Linked sale id number", compute="_compute_linked_sale_line"
    )
    linked_sale_line_sequence = fields.Integer(
        string="Linked sale sequence", compute="_compute_linked_sale_line"
    )

    @api.depends("move_dest_ids")
    def _compute_linked_sale_line(self):
        for line in self:
            sale_lines = (
                line.move_dest_ids
                and [x.sale_line_id for x in line.move_dest_ids]
                or False
            )
            if sale_lines:
                line.linked_sale_line_id_number = abs(1 - sale_lines[0].id)
                line.linked_sale_line_sequence = sale_lines[0].sequence
