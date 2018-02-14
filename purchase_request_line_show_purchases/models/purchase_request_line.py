# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, fields, models, exceptions, _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class PurchaseRequestLine(models.Model):
    
    # 1. Private attributes
    _inherit = 'purchase.request.line'

    # 2. Fields declaration
    purchase_order_ids = fields.Many2many(
        compute='_get_purchase_order_ids',
        comodel_name='purchase.order',
        string='Purchase Orders',
        readonly=True
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    def _get_purchase_order_ids(self):
        for request_line in self:
            request_line.purchase_order_ids = [po_line.order_id.id for po_line in request_line.purchase_lines]

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
