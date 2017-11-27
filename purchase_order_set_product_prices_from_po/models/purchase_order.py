# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    def validate_currencies(self, purchase_currency, product_currency):
        # Prevent cost price update if e.g. the product cost price is in EUR and PO price is in USD.
        # You can override this function if you use community modules that allow setting the product's cost price to
        # differ from the base currency.

        if purchase_currency.id != product_currency.id:
            raise exceptions.ValidationError(_("Cannot update cost price that is in {} when purchasing it in {}.").format(product_currency.name, purchase_currency.name))

    @api.multi
    def set_cost_prices(self):
        # Iterate through the checked PO lines and set their cost prices in the catalog to match the prices on the lines.
        # Raise an exception if the valuation/costing settings indicate that manual updates should not be done.
        self.ensure_one()

        if not self.order_line:
            raise exceptions.ValidationError(_('Please add some Purchase Order lines first.'))

        if not [line for line in self.order_line if line.update_price]:
            raise exceptions.ValidationError(_("Please check the 'Update Cost Price' field on some Purchase Order lines first."))
        

        for po_line in self.order_line:
            if po_line.update_price and po_line.product_id:

                self.validate_currencies(self.currency_id, po_line.product_id.currency_id)

                if po_line.product_id.valuation == 'real_time' and po_line.product_id.cost_method in ['standard', 'average']:
                    # This domain condition is the same as what makes the price_unit field readonly on the product form.
                    raise exceptions.ValidationError(_('Cost price should not be updated manually if Real-Time Inventory Valuation is in use together with Standard Price or Average Price costing.'))
                else:
                    po_line.product_id.standard_price = po_line.price_unit

        return {}