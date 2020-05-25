from odoo import api, fields, models, exceptions, _


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    project_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Project',
        readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}
    )

    @api.multi
    def set_line_analytic(self):

        purchase_order_line_model = self.env['purchase.order.line']
        analytic_account_model = self.env['account.analytic.account']

        for record in self:

            if not record.project_id:
                error = _('Please select a project first')
                raise exceptions.UserError(error)

            for line in record.order_line:
                line.account_analytic_id = record.project_id.id

                # If stock_location_analytic_account and
                # purchase_location_by_line are installed,
                # set the line destination location also
                if hasattr(
                    purchase_order_line_model, 'location_dest_id'
                ) and hasattr(analytic_account_model, 'default_location_id'):

                    line.location_dest_id = \
                        line.account_analytic_id.default_location_id.id \
                        or False
