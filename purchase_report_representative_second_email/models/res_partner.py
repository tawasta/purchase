from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    representative_email = fields.Char(string="Representative Email")
