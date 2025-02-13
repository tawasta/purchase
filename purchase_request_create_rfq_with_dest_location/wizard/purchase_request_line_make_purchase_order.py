from odoo import api, models


class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):
    _inherit = "purchase.request.line.make.purchase.order"

    @api.model
    def _prepare_purchase_order_line(self, po, item):
        """Assign Destination location to PO line from
        purchase request's Location field"""
        po_line_data = super()._prepare_purchase_order_line(po, item)

        pq_line = item and item.line_id or False
        request = pq_line and pq_line.request_id or False

        if request and request.stock_location_id:
            po_line_data["location_dest_id"] = request.stock_location_id.id

        return po_line_data

    @api.model
    def _get_order_line_search_domain(self, order, item):
        """Do not merge PO lines which have different destination locations"""
        order_line_data = super()._get_order_line_search_domain(order, item)

        location = item.request_id.stock_location_id.id

        order_line_data.append(("location_dest_id", "=", location))

        return order_line_data
