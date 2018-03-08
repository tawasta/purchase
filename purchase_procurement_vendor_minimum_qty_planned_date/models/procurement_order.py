# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.tools.translate import _
import datetime

class ProcurementOrder(osv.osv):

    _inherit = 'procurement.order'

    def _get_purchase_order_date(self, cr, uid, procurement, company, 
        schedule_date, context=None):
        ''' Calculate the date of the PO to be lead time amount of days
        backwards from the PO line scheduled date'''
        supplierinfo_model = self.pool['product.supplierinfo']
        args = self._get_supplier_args(cr, uid, procurement, context)

        qty_matching_supplier = supplierinfo_model.search(cr, uid, 
            args=args, limit=1, context=context)

        lead_time = qty_matching_supplier \
            and supplierinfo_model.browse(
                cr, uid, qty_matching_supplier[0], context
            ).delay or False

        if lead_time:
            lead_time_date = schedule_date - datetime.timedelta(days=lead_time)
            return lead_time_date
        else:
            # If no supplier was found, fallback to core functionality
            return super(ProcurementOrder, self)._get_purchase_order_date(cr, uid,
                procurement, company, schedule_date, context)