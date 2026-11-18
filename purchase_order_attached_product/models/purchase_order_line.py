# Copyright 2022 Tecnativa - David Vidal
# Copyright 2026 Futural
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
# Adapted from OCA/sale-workflow/sale_attached_product
# for purchase orders in November 2026.
from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _name = "purchase.order.line"
    _inherit = ["purchase.order.line", "purchase.attached.product.mixin"]

    is_attached_line = fields.Boolean(
        help="Flag products that are attached to their main counterpart"
    )

    attached_from_line_id = fields.Many2one(
        comodel_name="purchase.order.line", copy=False
    )
    attached_line_ids = fields.One2many(
        comodel_name="purchase.order.line",
        inverse_name="attached_from_line_id",
    )

    def _get_attached_products(self):
        """Return the line product's attached products allowed in the line company."""
        return self.product_id.product_tmpl_id.purchase_attached_product_ids.filtered(
            lambda x: not x.company_id or x.company_id == self.company_id
        )

    def _get_attached_line_uom_qty(self, attached_line):
        """Return the unit and quantity of an attached line: the main line's unit
        when the attached product allows it, otherwise the main line quantity
        converted to the attached product's unit."""
        self.ensure_one()
        # _origin: on a new (unsaved) line the allowed units are NewId copies,
        # which never match the main line's real unit.
        if self.product_uom_id in attached_line.allowed_uom_ids._origin:
            return self.product_uom_id, self.product_qty
        product_uom = attached_line.product_id.uom_id
        return product_uom, self.product_uom_id._compute_quantity(
            self.product_qty, product_uom
        )

    @api.model_create_multi
    def create(self, vals_list):
        """Resync the attached lines of the parent POs that got new lines."""
        if self._check_skip_attached_product_refresh():
            return super().create(vals_list)
        self_ctx = self.with_context(skip_auto_refresh_purchase_attached_product=True)
        lines = super(PurchaseOrderLine, self_ctx).create(vals_list)
        lines.order_id.recompute_attached_products()
        return lines

    def write(self, vals):
        """Resync the attached lines of the old and new parent POs when a trigger
        field changed."""
        if self._check_skip_attached_product_refresh():
            return super().write(vals)
        old_data = self._get_recs_data()
        old_orders = self.order_id
        self_ctx = self.with_context(skip_auto_refresh_purchase_attached_product=True)
        res = super(PurchaseOrderLine, self_ctx).write(vals)
        new_data = self._get_recs_data()
        new_orders = self.order_id
        if old_data != new_data:
            (old_orders | new_orders).recompute_attached_products()
        return res

    def unlink(self):
        """Resync the attached lines of the parent POs that lost lines."""
        if self._check_skip_attached_product_refresh():
            return super().unlink()
        orders = self.order_id
        self_ctx = self.with_context(skip_auto_refresh_purchase_attached_product=True)
        res = super(PurchaseOrderLine, self_ctx).unlink()
        orders.recompute_attached_products()
        return res

    @api.model
    def _get_auto_refresh_attached_product_triggers(self) -> set:
        """Line fields whose change triggers an attached lines resync."""
        triggers = super()._get_auto_refresh_attached_product_triggers()
        triggers.update({"product_id", "product_uom_id", "product_qty"})
        return triggers
