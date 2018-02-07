# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.tools.translate import _


class ProcurementOrder(osv.osv):

    _inherit = 'procurement.order'

    def _get_product_supplier(self, cr, uid, procurement, context=None):
        ''' Try to find a supplier with minimum delivery qty < required qty '''
        supplierinfo_model = self.pool['product.supplierinfo']
        args = \
            [('product_tmpl_id', '=', procurement.product_id.product_tmpl_id.id), 
             ('company_id', '=', procurement.company_id.id),
             ('min_qty', '<=', procurement.product_qty)]

        qty_matching_supplier = supplierinfo_model.search(cr, uid, 
            args=args, limit=1, context=context)

        if qty_matching_supplier:
            return supplierinfo_model.browse(cr, uid, qty_matching_supplier[0], 
                context=context).name
        
        else:
            # If no supplier was found, fallback to core functionality
            return super(ProcurementOrder, self)._get_product_supplier(cr, uid,
                procurement, context)