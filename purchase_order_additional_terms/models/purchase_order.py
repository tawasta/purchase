from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange("partner_id")
    def onchange_partner_id_additional_term(self):
        # If the partner has an additional term defined,
        # suggest it as a default
        if self.partner_id and self.partner_id.additional_term_id:
            self.additional_term_id = self.partner_id.additional_term_id.id

    additional_term_id = fields.Many2one(
        comodel_name="res_partner_additional_terms.term",
        string="Additional Term",
    )
