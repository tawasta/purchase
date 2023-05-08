from odoo import models


class ProductProduct(models.Model):

    _inherit = "product.product"

    def action_view_po(self):
        """Change to the opening view so that the all purchases will be shown"""
        action = super().action_view_po()

        context = action.get("context")

        # Check if context key has been set
        if context and context.get("search_default_later_than_a_year_ago"):
            action["context"]["search_default_later_than_a_year_ago"] = False

        return action
