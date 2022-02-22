
from odoo import models


class StockRule(models.Model):

    _inherit = 'stock.rule'

    def _make_po_get_domain(self, values, partner):
        """ Adds Sale Order condition for new purchase orders """
        domain = super(StockRule, self)._make_po_get_domain(values, partner)
        group = values.get('group_id')
        sale = group and group.sale_id
        domain += (
            ('original_sale_id', '=', sale.id),
        )

        return domain
