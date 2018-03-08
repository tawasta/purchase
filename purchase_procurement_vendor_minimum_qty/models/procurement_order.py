# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.tools.translate import _
import datetime

class ProcurementOrder(osv.osv):

    _inherit = 'procurement.order'

    def _get_supplier_args(self, cr, uid, procurement, context=None):
        '''Returns commonly used search arguments for finding a suitable 
        supplier that can provide the desired quantity'''
        return [('product_tmpl_id', '=', 
                 procurement.product_id.product_tmpl_id.id), 
                ('company_id', '=', procurement.company_id.id),
                ('min_qty', '<=', procurement.product_qty)]

    def _get_product_supplier(self, cr, uid, procurement, context=None):
        ''' Try to find a supplier with minimum delivery qty < required qty '''
        supplierinfo_model = self.pool['product.supplierinfo']
        args = self._get_supplier_args(cr, uid, procurement, context)

        qty_matching_supplier = supplierinfo_model.search(cr, uid, 
            args=args, limit=1, context=context)

        if qty_matching_supplier:
            return supplierinfo_model.browse(cr, uid, qty_matching_supplier[0], 
                context=context).name
        else:
            # If no supplier was found, fall back to core functionality
            return super(ProcurementOrder, self)._get_product_supplier(cr, uid,
                procurement, context)

    def _get_po_line_values_from_proc(self, cr, uid, procurement, partner, 
        company, schedule_date, context=None):
        '''Override the PO line qty calculation to handle cases where the 
        supplier has been changed to another who can supply a smaller qty 
        than the default supplier. 
        
        This is to avoid having the line qty forced to be the minimum quantity 
        of the default supplier '''

        uom_obj = self.pool.get('product.uom')
        pricelist_obj = self.pool.get('product.pricelist')

        uom_id = procurement.product_id.uom_po_id.id
        pricelist_id = partner.property_product_pricelist_purchase.id

        res = super(ProcurementOrder, self)._get_po_line_values_from_proc(
            cr, uid, procurement, partner, company, schedule_date, context
        )

        # Try to find a supplier that supplies the desired quantity
        supplierinfo_model = self.pool.get('product.supplierinfo')
        args = self._get_supplier_args(cr, uid, procurement, context)

        supplier_ids = supplierinfo_model.search(
            cr, uid, args, limit=1, context=context
        )
        
        if not supplier_ids:
            # If none found, fall back to the default supplier
            args = \
                [('product_tmpl_id', '=', 
                  procurement.product_id.product_tmpl_id.id),
                ('company_id', '=', procurement.product_id.company_id.id)]

            supplier_ids = supplierinfo_model.search(
                cr, uid, args, limit=1, context=context
            )

        if supplier_ids:
            supplier = supplierinfo_model.browse(
                cr, uid, supplier_ids[0], context
            )
            qty = uom_obj._compute_qty(
                cr, uid, procurement.product_uom.id, 
                procurement.product_qty, uom_id
            )
            seller_qty = supplier[0].min_qty \
                if procurement.location_id.usage != 'customer' \
                else 0.0

            if seller_qty:
                qty = max(qty, seller_qty)

                # Recalculate also the price to be based on the new qty
                price = pricelist_obj.price_get(
                    cr, uid, [pricelist_id], procurement.product_id.id, qty, 
                    partner.id, dict(context, uom=uom_id)
                )[pricelist_id]

                res['product_qty'] = qty
                res['price_unit'] = price or 0.0

        return res