from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.onchange("product_qty", "product_uom")
    def _onchange_quantity(self):
        self.ensure_one()

        if self.product_id and not self.price_unit:
            # Could not find a supplier price. Suggest product standard price
            product = self.product_id

            price_unit = self.env["account.tax"]._fix_tax_included_price_company(
                product.standard_price,
                product.supplier_taxes_id,
                self.taxes_id,
                self.company_id,
            )

            if (
                product
                and price_unit
                and product.currency_id
                and product.currency_id != self.order_id.currency_id
            ):
                price_unit = product.currency_id.compute(
                    price_unit, self.order_id.currency_id
                )

            if product and self.product_uom and product.uom_po_id != self.product_uom:
                price_unit = product.uom_po_id._compute_price(
                    price_unit, self.product_uom
                )

            self.price_unit = price_unit
