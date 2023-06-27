from odoo import _, models
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    def button_confirm(self):

        for record in self:
            if not record.partner_ref:
                raise ValidationError(
                    _("Please add a vendor reference before confirming")
                )

        return super().button_confirm()
