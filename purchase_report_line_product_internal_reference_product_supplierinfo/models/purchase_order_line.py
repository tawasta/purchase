from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    product_supplier_name = fields.Char(
        compute="_compute_product_supplier_code_and_name",
    )

    product_supplier_code = fields.Char(
        compute="_compute_product_supplier_code_and_name",
    )

    @api.depends("product_id")
    def _compute_product_supplier_code_and_name(self):
        # Compute supplierinfo-based helper fields to indicate the product name
        # and code shown to the supplier
        for line in self:
            if line.product_id:
                seller = line.product_id._select_seller(
                    partner_id=line.order_id.partner_id,
                    date=line.date_order and fields.Date.from_string(line.date_order),
                    quantity=line.product_uom_qty,
                    uom_id=line.product_uom,
                )
                name = seller.product_name
                code = seller.product_code
            else:
                name = ""
                code = ""

            line.product_supplier_name = name
            line.product_supplier_code = code
