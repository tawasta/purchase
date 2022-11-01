from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    purchase_note = fields.Text(
        help="Default purchase order note",
    )
