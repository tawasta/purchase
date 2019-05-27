from odoo import models, fields, api


class PurchaseOrderLine(models.Model):

    _inherit = 'purchase.order.line'

    @api.multi
    def _compute_running_number(self):
        '''Assigns a running number to the PO line, starting from 1 onwards '''
        for line in self:
            po_lines = self.search(args=[('order_id', '=', line.order_id.id)],
                                   order='id')

            i = 1
            for po_line in po_lines:
                if po_line.id == line.id:
                    line.running_number = i
                    break
                i += 1

    running_number = fields.Integer(
        compute=_compute_running_number,
        string='Running Number'
    )
