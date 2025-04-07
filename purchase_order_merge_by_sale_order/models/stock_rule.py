from odoo import models


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _make_po_get_domain(self, company_id, values, partner):
        """Adds Sale Order condition for new purchase orders"""
        domain = super()._make_po_get_domain(company_id, values, partner)
        moves = values.get("move_dest_ids")
        sale_line = moves and moves[0].sale_line_id or False

        if sale_line:
            so_id = sale_line.order_id.id
            domain += (("original_sale_id", "=", so_id),)

        return domain
