from odoo import models


class StockRule(models.Model):

    _inherit = "stock.rule"

    def _make_po_select_supplier(self, values, suppliers):
        """ Override the core functionality and try to find a supplier with
        minimum delivery qty < required qty """
        for supplier in suppliers:
            moves = values.get("move_dest_ids")

            if not moves:
                continue
            move = moves[0]

            if supplier.min_qty <= move.product_qty:
                return supplier

        return super(StockRule, self)._make_po_select_supplier(values, suppliers)
