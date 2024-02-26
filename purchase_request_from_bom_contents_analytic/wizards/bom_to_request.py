from odoo import models, fields


class BomToRequest(models.TransientModel):
    _inherit = "purchase_request_from_bom_contents.bom_to_request"

    def _default_analytic_account_id(self):
        request_id = self.env["purchase.request"].browse(self._context.get("active_id"))
        return request_id.analytic_account_id

    def get_request_line_values(self, line, purchase_request_id):
        res = super(BomToRequest, self).get_request_line_values(
            line, purchase_request_id
        )

        if self.analytic_account_id:
            distr = dict()
            distr[self.analytic_account_id.id] = 100
            res["analytic_distribution"] = distr

        return res

    def get_line_domain(self, line, purchase_request_id):
        args = super(BomToRequest, self).get_line_domain(line, purchase_request_id)

        distr = dict()
        distr[self.analytic_account_id.id] = 100
        args.append(("analytic_distribution", "=", distr))

        return args

    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Analytic Account",
        default=lambda self: self._default_analytic_account_id(),
    )

    # Update help text to clarify analytic account handling
    combine_with_existing = fields.Boolean(
        help=(
            """If the same product already exists on the Purchase Request
              with the same analytic account, the quantities are merged."""
        )
    )
