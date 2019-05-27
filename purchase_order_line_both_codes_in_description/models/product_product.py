from odoo import models, _


class ProductProduct(models.Model):

    _inherit = 'product.product'

    def name_get(self):
        # Check context if name_get should be modified
        if self.env.context.get('replace_supplier_code', False) \
                and self.env.context.get('partner_id', False):

            product_model = self.env['product.product']
            supplierinfo_model = self.env['product.supplierinfo']

            # Run the core name_get to get names in the
            # "[MYCODE123] My Product" format
            res = super(ProductProduct,
                        self.with_context({'partner_id': False})).name_get()

            # The result is a list of immutable tuples in the format of
            # [(id1,name1), (id2,name2), ...], so create a placeholder list
            # for editing and returning
            new_res = []

            # Go through all the products and check if they have supplier
            # infos for the active partner

            for product in res:
                # Matching has to be done using the template if no variants
                # are used.
                template_id \
                    = product_model.browse(product[0]).product_tmpl_id.id
                args = [('product_tmpl_id', '=', template_id),
                        ('name.id', '=', self.env.context['partner_id'])]
                matching_supplierinfo = supplierinfo_model.search(args)

                if not matching_supplierinfo:
                    new_res.append(product)
                else:
                    # If a matching supplierinfo was found, check if it has
                    # a product code defined. If yes, show it as a new line,
                    # resulting in the complete format of
                    # "[MYCODE123] My Product
                    #  Vendor's code: VCODE987"
                    code = matching_supplierinfo[0].product_code
                    if code:
                        new_name = product[1] + _("\nVendor's code: {}") \
                            .format(code)
                        new_res.append((product[0], new_name))
                    else:
                        new_res.append(product)

            return new_res
        else:
            return super(ProductProduct, self).name_get()
