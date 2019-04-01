# -*- coding: utf-8 -*-


from openerp import api, models


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.onchange('fiscal_position')
    def onchange_partner_id_update_purchase_note(self):
        for record in self:
            if record.partner_id and record.partner_id.purchase_note:
                record.notes = record.partner_id.purchase_note
