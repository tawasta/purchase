from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _purchase_request_confirm_message(self):
        """Same function as original, but message_notify is used
        to avoid sending e-mails."""
        request_obj = self.env["purchase.request"]
        for po in self:
            requests_dict = {}
            for line in po.order_line:
                for request_line in line.sudo().purchase_request_lines:
                    request_id = request_line.request_id.id
                    if request_id not in requests_dict:
                        requests_dict[request_id] = {}
                    date_planned = "%s" % line.date_planned
                    data = {
                        "name": request_line.name,
                        "product_qty": line.product_qty,
                        "product_uom": line.product_uom.name,
                        "date_planned": date_planned,
                    }
                    requests_dict[request_id][request_line.id] = data
            for request_id in requests_dict:
                request = request_obj.sudo().browse(request_id)
                message = po._purchase_request_confirm_message_content(
                    request, requests_dict[request_id]
                )
                request.message_post(
                    message_type="comment",
                    body=message,
                    subtype_xmlid="mail.mt_note",
                )
        return True
