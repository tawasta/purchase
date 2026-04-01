from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    dest_address_id = fields.Many2one(
        "res.partner", string="Shipping Address", copy=False, store=True
    )
