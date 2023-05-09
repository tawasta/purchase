from odoo import models
from odoo.tools.float_utils import float_round


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

    def _compute_purchased_product_qty(self):
        domain = [
            ("order_id.state", "in", ["purchase", "done"]),
            ("product_id", "in", self.ids),
        ]
        order_lines = self.env["purchase.order.line"].read_group(
            domain, ["product_id", "product_uom_qty"], ["product_id"]
        )
        purchased_data = {
            data["product_id"][0]: data["product_uom_qty"] for data in order_lines
        }
        for product in self:
            if not product.id:
                product.purchased_product_qty = 0.0
                continue
            product.purchased_product_qty = float_round(
                purchased_data.get(product.id, 0),
                precision_rounding=product.uom_id.rounding,
            )
