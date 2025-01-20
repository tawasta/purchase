from odoo import api, models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    @api.onchange("partner_id", "company_id")
    def onchange_partner_id(self):
        """Set Delivery Address from Vendor if there is
        a Default Delivery Address"""
        res = super().onchange_partner_id()

        partner = self.partner_id
        delivery_address = partner and partner.default_partner_delivery_id or False

        if delivery_address:
            self.po_delivery_address_id = delivery_address

        return res

    @api.model
    def create(self, vals):
        partner_id = vals.get("partner_id", False)
        partner = self.env["res.partner"].browse(partner_id)

        if partner and partner.default_partner_delivery_id:
            vals["po_delivery_address_id"] = partner.default_partner_delivery_id.id

        return super().create(vals)
