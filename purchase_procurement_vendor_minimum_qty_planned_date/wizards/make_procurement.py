# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _
import datetime


class MakeProcurement(models.Model):

    _inherit = 'make.procurement'


    @api.onchange('product_id', 'qty')
    def onchange_product(self):
        '''New onchange that triggers on both product and quantity changes. 
        Suggests planned date based on the vendor's lead time. Vendor selection
        is done with same logic as in purchase_procurement_vendor_minimum_qty'''
        if self.product_id and self.product_id.seller_ids:
            # Try to find a supplier that supplies the desired quantity
            supplierinfo_model = self.env['product.supplierinfo']
            args = \
                [('product_tmpl_id', '=', self.product_id.product_tmpl_id.id), 
                ('company_id', '=', self.product_id.company_id.id),
                ('min_qty', '<=', self.qty)]

            supplier = supplierinfo_model.search(args, limit=1)
            
            if not supplier:
                # If none found, fall back to the default supplier
                args = \
                    [('product_tmpl_id', '=', self.product_id.product_tmpl_id.id), 
                    ('company_id', '=', self.product_id.company_id.id)]

                supplier = supplierinfo_model.search(args, limit=1)

            lead_time = supplier and supplier[0].delay

            if lead_time:
                lead_time_date \
                    = datetime.datetime.now() \
                    + datetime.timedelta(days=(lead_time+1))
                self.date_planned = lead_time_date.strftime('%Y-%m-%d')
