
# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class PurchaseRequestLine(models.Model):

    # 1. Private attributes
    _inherit = "purchase.request.line"

    # 2. Fields declaration
    availability_line_ids = fields.One2many(
        comodel_name='purchase.request.availability.line',
        inverse_name='request_line_id',
        string='Availability in other Stock Locations',
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
