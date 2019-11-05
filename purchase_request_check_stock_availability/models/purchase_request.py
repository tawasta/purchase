# -*- coding: utf-8 -*-


from odoo import fields, models
from timeit import default_timer as timer_ticker
import logging

_logger = logging.getLogger(__name__)


class PurchaseRequest(models.Model):

    _inherit = 'purchase.request'

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

    def check_stock_availability(self):

        start = timer_ticker()

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

                qty_available = False

                quants = self.env['stock.quant'].search([
                    ('location_id', '=', location.id),
                    ('product_id', '=', request_line.product_id.id),
                    ('qty', '>', 0)
                ])

                if quants:
                    for quant in quants:
                        qty_available += quant.qty
                    availability_line_model.create({
                        'request_id': self.id,
                        'request_line_id': request_line.id,
                        'available_qty': qty_available,
                        'location_id': location.id,
                    })

        end = timer_ticker()
        time_spent = end - start
        _logger.info(
            ("Time spent on purchase request's method check_stock_avaibility: "
             "%ss") % time_spent
        )

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
