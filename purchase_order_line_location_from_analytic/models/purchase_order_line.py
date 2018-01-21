# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, fields, models


# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class PurchaseOrderLine(models.Model):
    # 1. Private attributes
    _inherit = 'purchase.order.line'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    @api.onchange('account_analytic_id')
    def onchange_analytic_account_id(self):
        if self.account_analytic_id and self.account_analytic_id.location_ids:
            self.location_dest_id = \
                self.account_analytic_id.default_location_id.id
        else:
            self.location_dest_id = False

    # 6. CRUD methods
    @api.model
    def create(self, vals):
        analytic_id = vals.get('account_analytic_id', False)
        analytic = self.env['account.analytic.account'].browse(analytic_id)
        suggest_location = self.suggest_location(vals, analytic_id)

        if analytic and analytic.default_location_id and suggest_location:
            vals['location_dest_id'] = analytic.default_location_id.id

        return super(PurchaseOrderLine, self).create(vals)

    # 7. Action methods

    # 8. Business methods
    def suggest_location(self, vals, analytic_id):
        ''' Define cases where the destination location should be suggested
        when creating a new PO line '''

        destination_id = vals.get('location_dest_id', False)
        active_model = self._context.get('active_model', False)

        # This prevents destination getting automatically set when a user
        # creates a PO with a PO line where the destination field is
        # intentionally left empty
        if analytic_id and not destination_id and active_model \
            and active_model != 'purchase.order':
            return True
        else:
            return False
