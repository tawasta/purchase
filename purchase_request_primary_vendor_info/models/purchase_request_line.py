from odoo import fields, models

from odoo.addons import decimal_precision as dp


class PurchaseRequestLine(models.Model):
    _inherit = "purchase.request.line"

    primary_vendor_code = fields.Char(
        related="product_id.primary_supplierinfo_id.product_code",
        string="Supplier's Code",
    )

    primary_vendor_price = fields.Float(
        related="product_id.primary_supplierinfo_id.price",
        digits=dp.get_precision("Product Price"),
        string="Supplier's Price",
    )

    primary_vendor_currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="product_id.primary_supplierinfo_id.currency_id",
        string="Supplier's Currency",
    )
