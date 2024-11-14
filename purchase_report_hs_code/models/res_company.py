from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    always_show_hs_code = fields.Boolean(
        string="Always show HS code on print",
        default=False,
    )
    use_po_line_hs_code = fields.Boolean(
        string="Use HS codes directly from PO lines",
        default=False,
    )
