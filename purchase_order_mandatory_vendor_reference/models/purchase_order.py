from odoo import _, models
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def confirm_reminder_mail(self, confirmed_date=False):
        for record in self:
            if not record.partner_ref:
                raise ValidationError(
                    _("Please add a vendor reference before confirming")
                )

        return super().confirm_reminder_mail(confirmed_date)
