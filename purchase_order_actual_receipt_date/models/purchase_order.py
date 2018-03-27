# -*- coding: utf-8 -*-
from odoo import api, models, fields


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.depends('order_line.qty_received')
    def _compute_date_receipt_actual(self):
        for order in self:
            # All physical products have been delivered
            # and the field has not been previously set
            if all([l.qty_received >= l.product_qty for l
                    in order.order_line
                    if l.product_id.type != 'service']) and \
                    not order.date_receipt_actual:

                order.date_receipt_actual = fields.Datetime.now()

    date_receipt_actual = fields.Date(
        compute='_compute_date_receipt_actual',
        string='Actual Receipt Date',
        readonly=True,
        store=True,
        help='Date of receiving all the ordered products'
    )
