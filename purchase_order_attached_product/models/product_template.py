# Copyright 2022 Tecnativa - David Vidal
# Copyright 2026 Futural
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
# Adapted from OCA/sale-workflow/sale_attached_product
# for purchase orders in November 2026.
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    purchase_attached_product_ids = fields.Many2many(
        comodel_name="product.product",
        relation="product_template_purchase_attached_product_rel",
        string="Attached Purchase Products",
        help="Products that are added automatically to the purchase order with the "
        "same quantity",
    )
