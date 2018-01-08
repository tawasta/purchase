# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

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

    # 8. Business methods
