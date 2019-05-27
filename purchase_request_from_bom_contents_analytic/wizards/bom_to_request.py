from odoo import models, fields


class BomToRequest(models.TransientModel):

    _inherit = 'purchase_request_from_bom_contents.bom_to_request'

    def get_request_line_values(self, line, purchase_request_id):
        res = super(BomToRequest, self) \
            .get_request_line_values(line, purchase_request_id)

        res['analytic_account_id'] \
            = self.analytic_account_id and self.analytic_account_id.id or False

        return res

    def get_line_domain(self, line, purchase_request_id):
        args = super(BomToRequest, self) \
            .get_line_domain(line, purchase_request_id)

        args.append(
            ('analytic_account_id',
             '=',
             self.analytic_account_id and self.analytic_account_id.id or False)
        )
        return args

    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analytic Account'
    )

    # Update help text to clarify analytic account handling
    combine_with_existing = fields.Boolean(
        help=('''If the same product already exists on the Purchase Request
              with the same analytic account, the quantities are merged.''')
    )
