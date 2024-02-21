from odoo import _, models
from odoo.exceptions import UserError


class PurchaseRequestLine(models.Model):
    _inherit = "purchase.request.line"

    def _can_be_deleted(self):
        """Redefines OCA's _can_be_deleted-method to allow deletion of
        Purchase request lines if:
        - Purchase request is in Draft- or Approved-state"""
        self.ensure_one()
        return self.request_state == "draft" or self.request_state == "approved"

    def unlink(self):
        """Overrides unlink-method and just the text shown in UserError after
        _can_be_deleted is changed"""
        if self.mapped("purchase_lines"):
            raise UserError(
                _("You cannot delete a record that refers to purchase " "lines!")
            )
        for line in self:
            if not line._can_be_deleted():
                raise UserError(
                    _(
                        "You can only delete a purchase request line if "
                        "the purchase request is in draft or approved state."
                    )
                )
        return super(PurchaseRequestLine, self).unlink()
