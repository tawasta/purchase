from odoo import models, fields


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    def _get_buyer_id(self):
        return self.env.uid

    buyer_id = fields.Many2one(
        default=_get_buyer_id,
        comodel_name='res.users',
        string="Buyer"
    )
