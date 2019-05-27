from openerp import models, fields


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    description = fields.Text(
        string='Description',
        help='Internal notes'
    )
