from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange("partner_id")
    def onchange_partner(self):
        """Get the standard clause in partner's language"""
        if self.partner_id:
            self.standard_clause = (
                self.with_context(lang=self.partner_id.lang)
                .env["res.company"]
                .browse(self.company_id.id)
                .purchase_order_standard_clause
            )
        else:
            self.standard_clause = False

    standard_clause = fields.Text(string="Standard Clause")
