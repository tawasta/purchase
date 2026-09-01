from odoo import fields

from odoo.addons.purchase.models.purchase_order import PurchaseOrder


def button_confirm(self):
    for order in self:
        if order.state not in ["draft", "sent", "po_sent"]:
            continue
        order.order_line._validate_analytic_distribution()
        order._add_supplier_to_product()
        # Deal with double validation process
        if order._approval_allowed():
            order.button_approve()
        else:
            order.write({"state": "to approve"})
        if order.partner_id not in order.message_partner_ids:
            order.message_subscribe([order.partner_id.id])
    return True


def _update_order_line_info(self, product_id, quantity, **kwargs):
    """Update purchase order line information for a given product or create
    a new one if none exists yet.
    :param int product_id: The product, as a `product.product` id.
    :return: The unit price of the product, based on the pricelist of the
             purchase order and the quantity selected.
    :rtype: float
    """
    self.ensure_one()
    product_packaging_qty = kwargs.get("product_packaging_qty", False)
    product_packaging_id = kwargs.get("product_packaging_id", False)
    pol = self.order_line.filtered(lambda line: line.product_id.id == product_id)
    if pol:
        if product_packaging_qty:
            pol.product_packaging_id = product_packaging_id
            pol.product_packaging_qty = product_packaging_qty
        elif quantity != 0:
            pol.product_qty = quantity
        # HERE IS THE ONLY MODIFIED PART WHERE po_sent HAS BEEN ADDED
        elif self.state in ["draft", "sent", "po_sent"]:
            price_unit = self._get_product_price_and_data(pol.product_id)["price"]
            pol.unlink()
            return price_unit
        else:
            pol.product_qty = 0
    elif quantity > 0:
        pol = self.env["purchase.order.line"].create(
            {
                "order_id": self.id,
                "product_id": product_id,
                "product_qty": quantity,
                "sequence": (
                    (self.order_line and self.order_line[-1].sequence + 1) or 10
                ),  # put it at the end of the order
            }
        )
        seller = pol.product_id._select_seller(
            partner_id=pol.partner_id,
            quantity=pol.product_qty,
            date=pol.order_id.date_order
            and pol.order_id.date_order.date()
            or fields.Date.context_today(pol),
            uom_id=pol.product_uom,
        )
        if seller:
            # Fix the PO line's price on the seller's one.
            price = seller.price
            if seller.currency_id != self.currency_id:
                price = seller.currency_id._convert(seller.price, self.currency_id)
            pol.price_unit = price
            pol.discount = seller.discount
    return pol.price_unit_discounted


PurchaseOrder._update_order_line_info = _update_order_line_info
PurchaseOrder.button_confirm = button_confirm
