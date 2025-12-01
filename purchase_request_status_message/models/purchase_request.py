from odoo import _, models


class PurchaseRequest(models.Model):
    _inherit = "purchase.request"

    def button_to_approve(self):
        res = super().button_to_approve()

        for request in self:
            if request.assigned_to:
                send_partners = [request.assigned_to.partner_id.id]

                request.message_post_with_source(
                    "purchase_request_status_message.purchase_request_message_approval_layout",
                    subtype_xmlid="mail.mt_note",
                    subject=_("Approval request"),
                    render_values={
                        "name": request.name,
                        "partner": request.assigned_to.partner_id,
                        "record": request,
                    },
                    email_layout_xmlid="mail.mail_notification_light",
                    partner_ids=send_partners,
                    email_from=request.company_id.email,
                )
        return res

    def button_approved(self):
        res = super().button_approved()

        for request in self:
            send_partners = [request.company_id.partner_id.id]
            approved_by = request.assigned_to.partner_id

            request.message_post_with_source(
                "purchase_request_status_message.purchase_request_approved_message_layout",
                subtype_xmlid="mail.mt_note",
                subject=_("Approved request"),
                render_values={
                    "name": request.name,
                    "partner": request.company_id.partner_id,
                    "record": request,
                    "approved_by": approved_by.name,
                },
                email_layout_xmlid="mail.mail_notification_light",
                partner_ids=send_partners,
                email_from=request.company_id.email,
            )
        return res

    def button_rejected(self):
        res = super().button_rejected()

        for request in self:
            send_partners = [request.requested_by.partner_id.id]
            rejected_by = self.env.user.partner_id

            request.message_post_with_source(
                "purchase_request_status_message.purchase_request_reject_message_layout",
                subtype_xmlid="mail.mt_note",
                subject=_("Rejected request"),
                render_values={
                    "name": request.name,
                    "partner": request.requested_by.partner_id,
                    "record": request,
                    "rejected_by": rejected_by.name,
                },
                email_layout_xmlid="mail.mail_notification_light",
                partner_ids=send_partners,
                email_from=request.company_id.email,
            )
        return res
