from odoo import api, models, _


class PurchaseOrderLine(models.Model):

    _inherit = 'purchase.order.line'

    @api.model
    def create(self, values):
        line = super(PurchaseOrderLine, self).create(values)
        product_id = line.product_id
        prod_tmpl = product_id.product_tmpl_id
        # Purchase order's vendor
        vendor = line.order_id.partner_id
        # Search matching vendors from product
        seller_ids = prod_tmpl.seller_ids.search([('name.id', '=', vendor.id),
            ('product_tmpl_id.id', '=', prod_tmpl.id)])

        vendor_code = [x.product_code for x in seller_ids if x.product_code]

        if product_id and vendor_code:
            for code in vendor_code:
                line.name = line.name.replace(
                    '[{}]'.format(code), '[{}]'.format(prod_tmpl.default_code))
                if _("Vendor's code:") not in line.name:
                    line.name += _("\nVendor's code: {}").format(vendor_code[0])
        return line

    @api.multi
    @api.onchange('product_id')
    def onchange_product_id(self):
        """Same functionality with onchange for friendlier usability"""
        res = super(PurchaseOrderLine, self).onchange_product_id()
        product_id = self.product_id
        prod_tmpl = product_id.product_tmpl_id
        vendor = self.order_id.partner_id
        seller_ids = prod_tmpl.seller_ids.search([('name.id', '=', vendor.id),
            ('product_tmpl_id.id', '=', prod_tmpl.id)])

        vendor_code = [x.product_code for x in seller_ids if x.product_code]

        if product_id and vendor_code:
            for code in vendor_code:
                self.name = self.name.replace(
                    '[{}]'.format(code), '[{}]'.format(prod_tmpl.default_code))
                if _("Vendor's code:") not in self.name:
                    self.name += _("\nVendor's code: {}").format(vendor_code[0])
        return res
