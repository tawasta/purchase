from odoo import models, fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    supplier_incoterm_id = fields.Many2one(
        comodel_name='stock.incoterms',
        string='Supplier Incoterm',
        company_dependent=True
    )
