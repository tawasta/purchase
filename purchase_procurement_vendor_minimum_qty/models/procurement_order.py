# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class ProcurementOrder(models.Model):

    _inherit = 'procurement.order'

    def _make_po_select_supplier(self, suppliers):
        ''' Override the core functionality and try to find a supplier with 
        minimum delivery qty < required qty '''
        for supplier in suppliers:
            if supplier.min_qty <= self.product_qty:
                return supplier

        return super(ProcurementOrder, self)._make_po_select_supplier(suppliers)