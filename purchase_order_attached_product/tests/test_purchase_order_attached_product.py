# Copyright 2022 Tecnativa - David Vidal
# Copyright 2026 Futural
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
# Adapted from OCA/sale-workflow/sale_attached_product
# for purchase orders in November 2026.
from odoo import Command
from odoo.tests import Form, TransactionCase


class TestPurchaseOrderAttachedProduct(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # No need for tracking and we scratch some seconds
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.vendor = cls.env["res.partner"].create({"name": "Mr. Odoo"})
        cls.product_1 = cls.env["product.product"].create(
            {"name": "Test 1", "purchase_ok": True, "standard_price": 50}
        )
        cls.product_2 = cls.env["product.product"].create(
            {"name": "Test 2", "purchase_ok": True, "standard_price": 60}
        )
        cls.product_3 = cls.env["product.product"].create(
            {"name": "Test 3", "purchase_ok": True, "standard_price": 70}
        )
        cls.product_4 = cls.env["product.product"].create(
            {"name": "Test 4", "purchase_ok": True, "standard_price": 80}
        )
        cls.product_5 = cls.env["product.product"].create(
            {"name": "Test 5", "purchase_ok": True, "standard_price": 80}
        )
        cls.product_1.product_tmpl_id.purchase_attached_product_ids = (
            cls.product_2 + cls.product_3
        )
        cls.uom_unit = cls.env.ref("uom.product_uom_unit")
        cls.uom_pack_6 = cls.env.ref("uom.product_uom_pack_6")
        cls.product_1.product_tmpl_id.uom_ids = cls.uom_pack_6
        # We'll be using this purchase order
        purchase_form = Form(cls.env["purchase.order"])
        purchase_form.partner_id = cls.vendor
        cls.purchase = purchase_form.save()

    def _add_product(self, purchase, product, qty=1):
        """Auxiliar method to quickly add products to a purchase order"""
        purchase_form = Form(purchase)
        with purchase_form.order_line.new() as line_form:
            line_form.product_id = product
            line_form.product_qty = qty
        purchase_form.save()

    def _get_attached_lines(self, purchase):
        return purchase.order_line.filtered("is_attached_line")

    def _get_line(self, purchase, product):
        return purchase.order_line.filtered(lambda x: x.product_id == product)

    def _enable_auto_update(self):
        self.env["ir.config_parameter"].sudo().set_param(
            "purchase_order_attached_product.auto_update_attached_lines", True
        )

    def _add_main_line(self, uom, qty=1):
        """Add product 1 in the given unit to the purchase order"""
        self.purchase.write(
            {
                "order_line": [
                    Command.create(
                        {
                            "product_id": self.product_1.id,
                            "product_qty": qty,
                            "product_uom_id": uom.id,
                        }
                    )
                ]
            }
        )
        return self._get_line(self.purchase, self.product_1)

    def test_01_attach_product_modifiable(self):
        """Every time we add a product with attached products we'll adding extra lines
        automatically"""
        # When we add a product with attached products defined on it the module will add
        # as many lines as attached products
        self._add_product(self.purchase, self.product_1)
        product_1_line = self.purchase.order_line.filtered(
            lambda x: x.product_id == self.product_1
        )
        self.assertEqual(
            len(self.purchase.order_line),
            3,
            "Two extra lines should have been added automatically",
        )
        self.assertEqual(
            self._get_attached_lines(self.purchase).product_id,
            self.product_1.product_tmpl_id.purchase_attached_product_ids,
            "The attached lines products should correspond with those defined in the "
            "product",
        )
        # Once added, we can edit the lines independetly
        product_1_line.product_qty = 3
        self.assertTrue(
            all(x.product_qty == 1 for x in self._get_attached_lines(self.purchase))
        )
        # We can delete attached lines in this mode
        self.purchase.order_line.filtered(
            lambda x: x.product_id == self.product_2
        ).unlink()
        self.assertEqual(
            len(self.purchase.order_line),
            2,
            "The line should stay removed",
        )
        # Removing the main line will kill the optional ones anyway
        product_1_line.unlink()
        self.assertFalse(
            self._get_attached_lines(self.purchase), "There should be no attached lines"
        )

    def test_02_attach_product_auto_update(self):
        """Every time we add a product with attached products we'll adding extra lines
        automatically. Those lines will be persistent"""
        self.env["ir.config_parameter"].sudo().set_param(
            "purchase_order_attached_product.auto_update_attached_lines", True
        )
        # When we add a product with attached products defined on it the module will add
        # as many lines as attached products
        self._add_product(self.purchase, self.product_1)
        product_1_line = self.purchase.order_line.filtered(
            lambda x: x.product_id == self.product_1
        )
        self.assertEqual(
            len(self.purchase.order_line),
            3,
            "Two extra lines should have been added automatically",
        )
        self.assertEqual(
            self._get_attached_lines(self.purchase).product_id,
            self.product_1.product_tmpl_id.purchase_attached_product_ids,
            "The attached lines products should correspond with those defined in the "
            "product",
        )
        # When we change the line quantity, the lines change theirs as well
        product_1_line.product_qty = 3
        self.assertTrue(
            all(
                x.product_qty == product_1_line.product_qty
                for x in self._get_attached_lines(self.purchase)
            )
        )
        # When we delete an attached line, the module will recreate it to keep the
        # attached lines consitency
        self.purchase.order_line.filtered(
            lambda x: x.product_id == self.product_2
        ).unlink()
        self.assertEqual(
            len(self.purchase.order_line),
            3,
            "The removed line should be recreated",
        )
        # Adding another product doesn't have any effect on the rest
        self._add_product(self.purchase, self.product_4)
        self.assertEqual(
            len(self.purchase.order_line),
            4,
            "Product 4 doesn't have any attached products",
        )
        # Changing the main line product will invalidate the attached lines
        product_1_line.product_id = self.product_5
        self.assertEqual(
            len(self.purchase.order_line),
            2,
            "The new product doesn't have any attached products",
        )
        self.assertFalse(
            self._get_attached_lines(self.purchase), "There should be no attached lines"
        )
        # If we change it back, the attached lines will be added back as well
        product_1_line.product_id = self.product_1
        self.assertEqual(
            len(self.purchase.order_line),
            4,
            "The attached lines should be added again",
        )
        self.assertEqual(
            self._get_attached_lines(self.purchase).product_id,
            self.product_1.product_tmpl_id.purchase_attached_product_ids,
            "The attached lines products should correspond with those defined in the "
            "product",
        )
        # Removing the main line, removes the attached lines
        product_1_line.unlink()
        self.assertFalse(
            self._get_attached_lines(self.purchase), "There should be no attached lines"
        )

    def test_03_attached_line_price(self):
        """Attached lines get the product cost, or the vendor price and discount"""
        self.env["product.supplierinfo"].create(
            {
                "partner_id": self.vendor.id,
                "product_tmpl_id": self.product_3.product_tmpl_id.id,
                "price": 55,
                "discount": 10,
            }
        )
        self._add_product(self.purchase, self.product_1, qty=2)
        line_2 = self._get_line(self.purchase, self.product_2)
        line_3 = self._get_line(self.purchase, self.product_3)
        self.assertEqual(line_2.product_qty, 2)
        self.assertEqual(line_2.price_unit, 60, "No vendor price: product cost")
        self.assertEqual(line_3.product_qty, 2)
        self.assertEqual(line_3.price_unit, 55, "Vendor price")
        self.assertEqual(line_3.discount, 10, "Vendor discount")

    def test_04_attached_line_follows_main_unit(self):
        """The attached line gets the main line unit when its product allows it"""
        self.product_2.product_tmpl_id.uom_ids = self.uom_pack_6
        self._add_main_line(self.uom_pack_6)
        line_2 = self._get_line(self.purchase, self.product_2)
        self.assertEqual(line_2.product_uom_id, self.uom_pack_6)
        self.assertEqual(line_2.product_qty, 1)
        self.assertEqual(line_2.price_unit, 360, "Cost of a 6-pack")

    def test_05_attached_line_unit_fallback(self):
        """The main line quantity is converted to the attached product's unit when
        the attached product does not allow the main line unit"""
        self._add_main_line(self.uom_pack_6)
        line_3 = self._get_line(self.purchase, self.product_3)
        self.assertEqual(line_3.product_uom_id, self.uom_unit)
        self.assertEqual(line_3.product_qty, 6)
        self.assertEqual(line_3.price_unit, 70)

    def test_06_main_line_unit_change(self):
        """With auto update, attached lines follow a main line unit change and are
        priced in the new unit"""
        self._enable_auto_update()
        self.product_2.product_tmpl_id.uom_ids = self.uom_pack_6
        main_line = self._add_main_line(self.uom_unit)
        main_line.product_uom_id = self.uom_pack_6
        self.assertEqual(len(self.purchase.order_line), 3)
        line_2 = self._get_line(self.purchase, self.product_2)
        self.assertEqual(line_2.product_uom_id, self.uom_pack_6)
        self.assertEqual(line_2.product_qty, 1)
        self.assertEqual(line_2.price_unit, 360, "Repriced for a 6-pack")
        self.assertEqual(line_2.attached_from_line_id, main_line)
        line_3 = self._get_line(self.purchase, self.product_3)
        self.assertEqual(line_3.product_uom_id, self.uom_unit)
        self.assertEqual(line_3.product_qty, 6)
        self.assertEqual(line_3.price_unit, 70)

    def test_07_copy_order(self):
        """A duplicated order gets its own attached lines, once"""
        self._add_product(self.purchase, self.product_1)
        new_purchase = self.purchase.copy()
        self.assertEqual(len(self.purchase.order_line), 3)
        self.assertEqual(len(new_purchase.order_line), 3)
        new_main_line = self._get_line(new_purchase, self.product_1)
        new_attached_lines = self._get_attached_lines(new_purchase)
        self.assertEqual(new_attached_lines.product_id, self.product_2 + self.product_3)
        self.assertEqual(new_attached_lines.attached_from_line_id, new_main_line)

    def test_08_confirmed_order_unchanged(self):
        """Attached lines of a confirmed order are not changed, and no line removal
        is attempted"""
        self._enable_auto_update()
        self._add_product(self.purchase, self.product_1)
        self.purchase.button_confirm()
        self.assertEqual(self.purchase.state, "purchase")
        main_line = self._get_line(self.purchase, self.product_1)
        attached_lines = self._get_attached_lines(self.purchase)
        # Would remove the attached lines on an RFQ
        main_line.product_qty = 0
        # Would remove the product 3 line on an RFQ
        self.product_1.product_tmpl_id.purchase_attached_product_ids = self.product_2
        main_line.product_qty = 2
        self.assertEqual(self._get_attached_lines(self.purchase), attached_lines)
        self.assertEqual(attached_lines.mapped("product_qty"), [1, 1])

    def test_09_mutually_attached_products(self):
        """Products attached to each other do not add lines on every save"""
        self.product_2.product_tmpl_id.purchase_attached_product_ids = self.product_1
        self._add_product(self.purchase, self.product_1)
        self.assertEqual(len(self.purchase.order_line), 3)
        main_line = self._get_line(self.purchase, self.product_1)
        for qty in (2, 3):
            main_line.product_qty = qty
            self.assertEqual(len(self.purchase.order_line), 3)
