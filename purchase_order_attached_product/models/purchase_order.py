# Copyright 2022 Tecnativa - David Vidal
# Copyright 2026 Futural
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
# Adapted from OCA/sale-workflow/sale_attached_product
# for purchase orders in November 2026.
from collections import defaultdict

from odoo import api, fields, models

AUTO_UPDATE_PARAM = "purchase_order_attached_product.auto_update_attached_lines"
RFQ_STATES = ("draft", "sent", "to approve")


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = ["purchase.order", "purchase.attached.product.mixin"]

    def _get_attached_product_snapshot(self):
        """Trigger field values of all lines of these orders."""
        return self.order_line._get_attached_product_snapshot()

    def _get_attached_line_values_product(self, line, product):
        """Prepare the values for the attached line. This is used for creating or
        updating."""

        def _execute_onchanges(records, field_name):
            """Helper methods that executes all onchanges associated to a field."""
            for onchange in records._onchange_methods.get(field_name, []):
                for record in records:
                    onchange(record)

        # We prepare a new line and trigger the proper onchanges to ensure we get the
        # right line values (vendor price, taxes, planned date, etc.)
        order_line = self.order_line.new(
            {"order_id": self.id, "product_id": product.id}
        )
        _execute_onchanges(order_line, "product_id")
        # The unit and quantity are set after the product onchange, as that one
        # resets them to the vendor's minimum quantity and unit.
        uom, qty = line._get_attached_line_uom_qty(order_line)
        order_line.update({"product_uom_id": uom.id, "product_qty": qty})
        # The cache snapshot below does not run pending computes, so the vendor
        # price, discount and planned date are computed explicitly for this quantity.
        order_line._compute_price_unit_and_date_planned_and_name()

        _execute_onchanges(order_line, "product_qty")
        vals = order_line._convert_to_write(order_line._cache)
        vals.update({"is_attached_line": True, "attached_from_line_id": line.id})
        return vals

    def _create_attached_line(self, lines):
        """We create all the lines at once. This should be more performant"""
        vals_list = []
        for line in lines:
            for product in line._get_attached_products():
                vals_list.append(self._get_attached_line_values_product(line, product))
        if vals_list:
            self.with_context(skip_auto_refresh_purchase_attached_product=True).write(
                {"order_line": [fields.Command.create(vals) for vals in vals_list]}
            )

    def _cleanup_attached_lines(self):
        """Remove those line which main line is already removed or wich main line
        product attachment won't match its lines."""
        self.ensure_one()
        auto_update_attached_lines = (
            self.env["ir.config_parameter"].sudo().get_param(AUTO_UPDATE_PARAM)
        )
        lines = self.order_line.filtered("is_attached_line")
        lines.filtered(lambda x: not x.attached_from_line_id).unlink()
        if not auto_update_attached_lines:
            return
        # We also want to remove those lines which main product doesn't match anymore
        # but only when auto update is on
        lines_with_attachements = self.order_line.filtered("attached_line_ids")
        for line in lines_with_attachements:
            attached_products = line._get_attached_products()
            line.attached_line_ids.with_context(
                skip_auto_refresh_purchase_attached_product=True
            ).filtered(
                lambda x, attached_products=attached_products: x.product_id
                not in attached_products
            ).unlink()

    def _create_attached_lines(self):
        """New attached lines. After this, they'll be updated if there are changes in
        the main line."""
        self.ensure_one()
        # Attached lines are never main lines, otherwise products attached to each
        # other would add a new line on every save.
        self._create_attached_line(
            self.order_line.filtered(
                lambda x: not x.is_attached_line
                and not x.attached_line_ids
                and x._get_attached_products()
            )
        )

    def _update_attached_lines(self):
        """Update attached lines values related to their main line."""
        self.ensure_one()
        lines_with_attachements = self.order_line.filtered("attached_line_ids")
        lines_to_remove = self.env["purchase.order.line"]
        # Grouped by quantity to write each group at once
        lines_to_update = defaultdict(lambda: self.env["purchase.order.line"])
        missing_list = []
        for line in lines_with_attachements:
            # Lines with no qty can be considered to be removed.
            if not line.product_qty:
                lines_to_remove += line.attached_line_ids
                continue
            # Attached lines follow the main line unit and quantity
            for attached_line in line.attached_line_ids:
                uom, qty = line._get_attached_line_uom_qty(attached_line)
                if attached_line.product_uom_id != uom:
                    # Recreated: writing the unit of a saved line keeps the old unit
                    # price when the product has no vendor price.
                    lines_to_remove += attached_line
                    missing_list.append(
                        self._get_attached_line_values_product(
                            line, attached_line.product_id
                        )
                    )
                elif uom.compare(attached_line.product_qty, qty):
                    # Writing the quantity recomputes the vendor price
                    lines_to_update[qty] += attached_line
            attached_products = line._get_attached_products()
            # Create missing products, for example in the case of a deleted attached
            # line.
            missing_products = {
                p
                for p in attached_products
                if p not in line.attached_line_ids.product_id
            }
            for product in missing_products:
                missing_list.append(
                    self._get_attached_line_values_product(line, product)
                )
        for qty, attached_lines in lines_to_update.items():
            attached_lines.with_context(
                skip_auto_refresh_purchase_attached_product=True
            ).write({"product_qty": qty})
        lines_to_remove.with_context(
            skip_auto_refresh_purchase_attached_product=True
        ).unlink()
        self.with_context(skip_auto_refresh_purchase_attached_product=True).write(
            {"order_line": [fields.Command.create(vals) for vals in missing_list]}
        )

    def recompute_attached_products(self):
        """Recurrent method for recomputing attached lines. Always done in these three
        steps:

        1. A cleanup of orphaned attached lines or attached lines that doesn't match
           their parent attached products anymore.
        2. Creating new attached lines from lines which don't have them.
        3. Updating existing attached lines. Mainly for quantity"""
        auto_update_attached_lines = (
            self.env["ir.config_parameter"].sudo().get_param(AUTO_UPDATE_PARAM)
        )

        # Only RFQs: confirmed orders forbid deleting product lines and new lines
        # there would create unexpected receipts.
        rfq_orders = self.filtered(lambda x: x.state in RFQ_STATES and not x.locked)
        for order in rfq_orders:
            order._cleanup_attached_lines()
            order._create_attached_lines()
            if auto_update_attached_lines:
                order._update_attached_lines()

    def copy_data(self, default=None):
        """Leave the attached lines out of the copy: the copied main lines get new
        ones. Copied attached lines would be orphans, deleted in the middle of the
        line create while the caller still uses them."""
        default = dict(default or {})
        if "order_line" in default:
            return super().copy_data(default=default)
        default["order_line"] = []
        vals_list = super().copy_data(default=default)
        for order, vals in zip(self, vals_list, strict=True):
            main_lines = order.order_line.filtered(lambda x: not x.is_attached_line)
            vals["order_line"] = [
                fields.Command.create(line_vals)
                for line_vals in main_lines.sorted("id").copy_data()
            ]
        return vals_list

    @api.model_create_multi
    def create(self, vals_list):
        """Add the attached lines to orders created with their lines."""
        if self._check_skip_attached_product_refresh():
            return super().create(vals_list)
        orders = super().create(vals_list)
        orders.recompute_attached_products()
        return orders

    def write(self, vals):
        """Resync the attached lines once per order when a trigger field changed.
        The line-level resync is skipped during the write to avoid doing it twice."""
        if self._check_skip_attached_product_refresh():
            return super().write(vals)
        old_snapshot = self._get_attached_product_snapshot()
        self_ctx = self.with_context(skip_auto_refresh_purchase_attached_product=True)
        res = super(PurchaseOrder, self_ctx).write(vals)
        if self._get_attached_product_snapshot() != old_snapshot:
            self.recompute_attached_products()
        return res
