# -*- coding: utf-8 -*-
from odoo import models, fields


class PriceWizardLine(models.TransientModel):

    _name = 'purchase.order.to.vendor.price.wizard.line'
    _rec_name = 'wizard_id'

    wizard_id = fields.Many2one(
        comodel_name='purchase_order_set_vendor_prices_from_po.price_wizard',
        string='Parent Wizard'
    )

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product'
    )

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Vendor'
    )
