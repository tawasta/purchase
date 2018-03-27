# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class PurchaseRequest(models.Model):

    # 1. Private attributes
    _inherit = 'purchase.request'

    # 2. Fields declaration
    availability_line_ids = fields.One2many(
        comodel_name='purchase.request.availability.line',
        inverse_name='request_id',
        string='Available Products',
    )

    stock_picking_ids = fields.One2many(
        comodel_name='stock.picking',
        inverse_name='purchase_request_id',
        string='Internal Transfers',
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    def check_stock_availability(self):

        stock_location_model = self.env['stock.location']
        availability_line_model \
            = self.env['purchase.request.availability.line']

        # Clear current lines
        self.availability_line_ids = False

        # Get all locations where to search for the products
        args = self.get_stock_location_domain()
        locations_to_check = stock_location_model.search(args)

        # Iterate all lines on the PR, check their available quantities in
        # different stock locations, and create availability lines accordingly
        for request_line in self.line_ids:
            for location in locations_to_check:
                qty_available = request_line.product_id \
                    .with_context(location=location.id).qty_available

                if qty_available > 0:
                    availability_line_model.create({
                        'request_id': self.id,
                        'request_line_id': request_line.id,
                        'available_qty': qty_available,
                        'location_id': location.id,
                    })

    # 8. Business methods
    def get_stock_location_domain(self):
        ''' What stock locations should be included when checking if materials
        exist elsewhere. By default included ones are internal physical
        locations that are linked to an analytic account (i.e. are project
        locations) and belong to the same company. The location set on the
        purchase request is filtered out to avoid suggesting same source/target
        locations'''
        return [('company_id', '=', self.company_id.id),
                ('id', '!=', self.stock_location_id.id),
                ('usage', '=', 'internal'),
                ('analytic_account_id', '!=', False)]
