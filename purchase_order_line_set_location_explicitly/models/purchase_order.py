# -*- coding: utf-8 -*-
from odoo import models, api


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.multi
    def button_approve(self, force=False):
        '''When confirming a PO, set the lines' empty destination locations
        with the core method that returns the picking type's destination
        location (or the customer virtual location, if drop shipping
        is used)'''
        for line in self.order_line:
            if not line.location_dest_id:
                line.location_dest_id = self._get_destination_location()

        return super(PurchaseOrder, self).button_approve()
