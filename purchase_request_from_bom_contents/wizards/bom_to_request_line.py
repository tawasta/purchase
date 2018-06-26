# -*- coding: utf-8 -*-
from odoo import models, fields


class BomToRequestLine(models.TransientModel):

    _name = 'purchase_request_from_bom_contents.bom_to_request_line'
    _rec_name = 'product_id'

    wizard_id = fields.Many2one(
        comodel_name='purchase_request_from_bom_contents.bom_to_request',
        string='Parent Wizard'
    )

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product'
    )

    product_active = fields.Boolean(
        related='product_id.active',
        string='Product Active'
    )

    uom_id = fields.Many2one(
        comodel_name='product.uom',
        string='UoM'
    )

    qty = fields.Float(
        string='Quantity',
        digits=(6, 2)
    )

    notes = fields.Text(
        string='Notes'
    )
