from odoo import models, fields


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    purchase_order_ids = fields.One2many(
        string='Purchase order',
        comodel_name='purchase.order',
        inverse_name='sale_order_id',
    )
