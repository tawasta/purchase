from odoo import models, api


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.model
    def create(self, vals):
        if 'incoterm_id' not in vals and 'partner_id' in vals:
            partner = self.env['res.partner'].browse(vals['partner_id'])
            if partner and partner.supplier_incoterm_id:
                vals['incoterm_id'] = partner.supplier_incoterm_id.id

        return super(PurchaseOrder, self).create(vals)

    @api.onchange('partner_id')
    def onchange_partner_id_incoterm(self):
        if self.partner_id and self.partner_id.supplier_incoterm_id:
            self.incoterm_id = self.partner_id.supplier_incoterm_id.id
