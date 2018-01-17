# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

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
            self.location_dest_id = self.account_analytic_id.location_ids[0].id
        else: 
            self.location_dest_id = False

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
