from odoo import models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def allocate(self):
        """The same function as in purchase_request module, but messages are sent
        as internal notes."""
        for ml in self.filtered(
            lambda m: m.exists() and m.move_id.purchase_request_allocation_ids
        ):
            to_allocate_qty = ml.quantity
            to_allocate_uom = ml.product_uom_id
            for allocation in ml.move_id.purchase_request_allocation_ids.sudo():
                allocated_qty = 0.0
                if allocation.open_product_qty and to_allocate_qty:
                    to_allocate_uom_qty = to_allocate_uom._compute_quantity(
                        to_allocate_qty, allocation.product_uom_id
                    )
                    allocated_qty = min(
                        allocation.open_product_qty, to_allocate_uom_qty
                    )
                    allocation.allocated_product_qty += allocated_qty
                    to_allocate_uom_qty -= allocated_qty
                    to_allocate_qty = allocation.product_uom_id._compute_quantity(
                        to_allocate_uom_qty, to_allocate_uom
                    )

                request = allocation.purchase_request_line_id.request_id
                if allocated_qty:
                    message_data = self._prepare_message_data(
                        ml, request, allocated_qty
                    )
                    message = self._purchase_request_confirm_done_message_content(
                        message_data
                    )
                    if message:
                        request.message_post(
                            message_type="comment",
                            body=message,
                            subtype_xmlid="mail.mt_note",
                        )

                    picking_message = self._picking_confirm_done_message_content(
                        message_data
                    )
                    ml.move_id.picking_id.message_post(
                        message_type="comment",
                        body=picking_message,
                        subtype_xmlid="mail.mt_note",
                    )

                allocation._compute_open_product_qty()
