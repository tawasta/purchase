from odoo import _, api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[("po_sent", "PO Sent"), ("to approve",)])

    def print_purchase_order(self):
        self.write({"state": "po_sent"})
        return self.env.ref("purchase.action_report_purchase_order").report_action(
            self.id
        )

    def _track_subtype(self, init_values):
        subtypes = super()._track_subtype(init_values=init_values)

        if "state" in init_values and self.state == "po_sent":
            return self.env.ref("purchase_order_po_sent_status.mt_po_sent")
        return subtypes

    def action_send_po(self):
        """
        Open up a wizard to send Purchase Order email
        """
        self.ensure_one()
        ir_model_data = self.env["ir.model.data"]
        try:
            template_id = ir_model_data._xmlid_lookup(
                "purchase.email_template_edi_purchase_done"
            )[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data._xmlid_lookup(
                "mail.email_compose_message_wizard_form"
            )[1]
        except ValueError:
            compose_form_id = False
        ctx = dict(self.env.context or {})
        layout_xmlid = "mail.mail_notification_layout_with_responsible_signature"
        # Note how mark_po_as_sent is set as True. This is used in message_post method
        ctx.update(
            {
                "default_model": "purchase.order",
                "default_res_ids": self.ids,
                "default_template_id": template_id,
                "default_composition_mode": "comment",
                "default_email_layout_xmlid": layout_xmlid,
                "force_email": True,
                "mark_po_as_sent": True,
            }
        )

        lang = self.env.context.get("lang")
        if {"default_template_id", "default_model", "default_res_id"} <= ctx.keys():
            template = self.env["mail.template"].browse(ctx["default_template_id"])
            if template and template.lang:
                lang = template._render_lang([ctx["default_res_id"]])[
                    ctx["default_res_id"]
                ]

        self = self.with_context(lang=lang)
        ctx["model_description"] = _("Purchase Order")

        return {
            "name": _("Compose Email"),
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "mail.compose.message",
            "views": [(compose_form_id, "form")],
            "view_id": compose_form_id,
            "target": "new",
            "context": ctx,
        }

    @api.returns("mail.message", lambda value: value.id)
    def message_post(self, **kwargs):
        if self.env.context.get("mark_po_as_sent"):
            self.filtered(lambda o: o.state == "sent").write({"state": "po_sent"})
        po_ctx = {
            "mail_post_autofollow": self.env.context.get("mail_post_autofollow", True)
        }
        if self.env.context.get("mark_po_as_sent") and "notify_author" not in kwargs:
            kwargs["notify_author"] = self.env.user.partner_id.id in (
                kwargs.get("partner_ids") or []
            )

        return super(PurchaseOrder, self.with_context(**po_ctx)).message_post(**kwargs)
