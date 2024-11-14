from odoo import api, fields, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    hs_code_id = fields.Many2one(
        string="H.S. Code",
        comodel_name="hs.code",
        default=lambda self: self._default_hs_code_id(),
        store=True,
    )

    def _default_hs_code_id(self):
        return self.product_id.hs_code_id

    @api.onchange("product_id")
    def onchange_product_id(self):
        if self.product_id:
            self.hs_code_id = self.product_id.hs_code_id or False

        return super().onchange_product_id()

    def set_line_hs_code(self):
        """Helper function"""
        for line in self:
            line.hs_code_id = line.product_id.hs_code_id or False
