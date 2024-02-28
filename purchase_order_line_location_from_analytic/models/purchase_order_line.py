from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.onchange("analytic_distribution")
    def onchange_analytic_account_id(self):
        account_id = False

        for account, percentage in (self.analytic_distribution or {}).items():
            account_id = self.env["account.analytic.account"].browse(
                map(int, account.split(","))
            )

        if account_id and account_id.default_location_id:
            self.location_dest_id = account_id.default_location_id
        else:
            self.location_dest_id = False

    # 6. CRUD methods
    @api.model
    def create(self, vals):
        account_id = False
        distribution = vals.get("analytic_distribution", False)

        for account, percentage in (distribution or {}).items():
            account_id = self.env["account.analytic.account"].browse(
                map(int, account.split(","))
            )

        suggest_location = self.suggest_location(vals, account_id)

        if account_id and account_id.default_location_id and suggest_location:
            vals["location_dest_id"] = account_id.default_location_id.id

        return super(PurchaseOrderLine, self).create(vals)

    # 8. Business methods
    def suggest_location(self, vals, analytic_id):
        """Define cases where the destination location should be suggested
        when creating a new PO line"""

        destination_id = vals.get("location_dest_id", False)

        # This prevents destination getting automatically set when a user
        # creates a PO with a PO line where the destination field is
        # intentionally left empty
        if analytic_id and not destination_id:
            return True
        else:
            return False
