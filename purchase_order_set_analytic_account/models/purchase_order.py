from odoo import exceptions, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def set_line_analytic(self):
        for order in self:
            ctx_project = self.env["project.project"].browse(
                self.env.context.get("project_id")
            )
            project_lines = order.order_line.filtered(
                lambda line, ctx_project=ctx_project: not line.display_type
                and (ctx_project or line.order_id.project_id)
            )
            project = order.project_id
            if not project:
                error = self.env._("Please select a project first")
                raise exceptions.UserError(error)

            for line in project_lines:
                line.analytic_distribution = project._get_analytic_distribution()

                account_id = project.account_id

                # If stock_location_analytic_account and
                # purchase_location_by_line are installed,
                # set the line destination location also
                if (
                    hasattr(self.env["purchase.order.line"], "location_dest_id")
                    and hasattr(
                        self.env["account.analytic.account"], "default_location_id"
                    )
                    and account_id
                ):
                    line.location_dest_id = account_id.default_location_id.id or False
