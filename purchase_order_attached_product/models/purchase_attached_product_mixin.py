# Copyright 2022 Tecnativa - David Vidal
# Copyright 2026 Futural
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
# Adapted from OCA/sale-workflow/sale_attached_product
# for purchase orders in November 2026.

from odoo import api, models


class PurchaseAttachedProductMixin(models.AbstractModel):
    _name = "purchase.attached.product.mixin"
    _description = "Mixin class for purchase attached product features"

    @api.model
    def _get_auto_refresh_attached_product_triggers(self) -> set:
        """Returns set of PO line fields which trigger the recomputation.
        The method is overriden in the PO line model
        """
        return set()

    def _check_skip_attached_product_refresh(self):
        """Checks whether refresh should be skipped

        Hook method to be overridden if necessary
        :return: True if auto-refresh should be skipped
        """

        return self.env.context.get("skip_auto_refresh_purchase_attached_product")
