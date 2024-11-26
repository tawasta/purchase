from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    always_show_hs_code = fields.Boolean(
        string="Always show HS code on print",
        related="company_id.always_show_hs_code",
        readonly=False,
    )
    use_po_line_hs_code = fields.Boolean(
        string="Use HS codes directly from PO lines",
        related="company_id.use_po_line_hs_code",
        readonly=False,
    )
