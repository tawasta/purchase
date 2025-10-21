from odoo import fields, models


class SaleToRequestLine(models.TransientModel):
    _name = "purchase_request_from_sale_contents.sale_to_request_line"
    _rec_name = "product_id"

    wizard_id = fields.Many2one(
        comodel_name="purchase_request_from_sale_contents.sale_to_request",
        string="Parent Wizard",
    )

    product_id = fields.Many2one(comodel_name="product.product", string="Product")

    product_active = fields.Boolean(
        related="product_id.active", string="Product Active"
    )

    uom_id = fields.Many2one(comodel_name="uom.uom", string="UoM")

    qty = fields.Float(string="Quantity", digits=(6, 2))
