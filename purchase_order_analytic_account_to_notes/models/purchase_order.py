# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.multi
    def button_confirm(self):
        for record in self:
            if record.project_id:
                if record.notes:
                    record.notes = \
                        '%s\n%s' % (record.notes, record.project_id.name)
                else:
                    record.notes = record.project_id.name

        return super(PurchaseOrder, self).button_confirm()
