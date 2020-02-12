# -*- coding: utf-8 -*-
from odoo import api, models


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        """
        Override to disable grouping if analytic account differs.
        :return:
        """
        make_po_conditions = {
            'partner_id', 'state', 'picking_type_id', 'company_id',
            'dest_address_id',
        }

        # Filter out PO:s that have a project
        # when creating a PO from a procurement
        if (self.env.context and
                self.env.context.get('grouping') and
                make_po_conditions.issubset(set(x[0] for x in args))):

            args.append(('project_id', '=', False))

        return super(PurchaseOrder, self).search(
            args, offset=offset, limit=limit, order=order, count=count)
