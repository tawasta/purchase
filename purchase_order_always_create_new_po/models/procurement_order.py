# -*- coding: utf-8 -*-


from odoo import models


class ProcurementOrder(models.Model):

    _inherit = 'procurement.order'

    def _make_po_get_domain(self, partner):
        res = super(ProcurementOrder, self)._make_po_get_domain(partner)
        res = list(res)
        res.append(('partner_id', '=', False))
        res = tuple(res)

        return res
