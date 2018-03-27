# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models, exceptions, _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class PurchaseRequest(models.Model):

    # 1. Private attributes
    _inherit = 'purchase.request'

    # 2. Fields declaration
    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Project',
        readonly=True,
        states={'draft': [('readonly', False)]}
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    @api.one
    def set_line_analytic(self):
        if not self.analytic_account_id:
            error = _('Please select a project first')
            raise exceptions.UserError(error)

        for line in self.line_ids:
            line.analytic_account_id = self.analytic_account_id.id

    # 8. Business methods
