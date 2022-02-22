
from odoo import api, fields, models


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    original_sale_id = fields.Many2one('sale.order',
        string="Created from Sale:")

    @api.model
    def create(self, values):
        """ Sale Order record is added based on PO origin text """
        sale_id = self.sudo().env['sale.order'].search(
                [('name','=',values.get('origin'))])
        if sale_id:
            values['original_sale_id'] = sale_id.id

        return super().create(values)
