# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models, exceptions, _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class PurchaseOrder(models.Model):

    # 1. Private attributes
    _inherit = 'purchase.order'

    # 2. Fields declaration

    # This is just a helper field to be used when passing a default value to PO lines in XML,
    # since the context attribute does not accept referencing the AA using
    # a syntax like { 'default_x': project_id.analytic_account_id } there
    analytic_account_id = fields.Many2one(related='project_id.analytic_account_id', string='Analytic Account')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    @api.one
    def set_line_analytic(self):

        purchase_order_line_model = self.env['purchase.order.line']
        analytic_account_model = self.env['account.analytic.account']

        if not self.project_id:
            error = _('Please select a project first')
            raise exceptions.UserError(error)

        for line in self.order_line:
            line.account_analytic_id = self.analytic_account_id.id

            # If stock_location_analytic_account and purchase_location_by_line
            # are installed, set the line destination location also
            if hasattr(purchase_order_line_model, 'location_dest_id') \
                and hasattr(analytic_account_model, 'default_location_id'):

                line.location_dest_id = \
                    line.account_analytic_id.default_location_id.id or False

    # 8. Business methods