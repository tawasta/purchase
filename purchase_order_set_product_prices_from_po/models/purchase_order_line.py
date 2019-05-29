from odoo import models, fields


class PurchaseOrderLine(models.Model):

    _inherit = 'purchase.order.line'

    update_price = fields.Boolean(
        string='Update Cost Price',
        help=("Checked lines' products will have their Cost Prices updated "
              "according to the price on the line when Purchase Order's "
              "'Update Prices' button is clicked.")
    )
