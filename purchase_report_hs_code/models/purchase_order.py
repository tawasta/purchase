from odoo import fields, models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    show_hs_code_on_print = fields.Boolean(
        string="Show HS Codes on a print",
        default=lambda self: self.env.company.always_show_hs_code,
        copy=False,
    )

    def set_show_hs_code_on_print_as_true(self):
        """Helper function"""
        for order in self:
            order.show_hs_code_on_print = True

    def set_show_hs_code_on_print_as_false(self):
        """Helper function"""
        for order in self:
            order.show_hs_code_on_print = False
