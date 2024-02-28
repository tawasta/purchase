from odoo import api, fields, models, exceptions, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    project_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Project",
        readonly=True,
    )

    def set_line_analytic(self):
        purchase_order_line_model = self.env["purchase.order.line"]
        analytic_account_model = self.env["account.analytic.account"]

        for purchase in self:
            if not purchase.project_id:
                error = _("Please select a project first")
                raise exceptions.UserError(error)

            account_id = purchase.project_id
            distr = dict()
            distr[account_id.id] = 100

            for line in purchase.order_line:
                line.analytic_distribution = distr

                # If stock_location_analytic_account and
                # purchase_location_by_line are installed,
                # set the line destination location also
                if hasattr(purchase_order_line_model, "location_dest_id") and hasattr(
                    analytic_account_model, "default_location_id"
                ):
                    line.location_dest_id = account_id.default_location_id.id or False
