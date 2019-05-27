from odoo import models, fields, api, _


class PriceWizard(models.TransientModel):

    _name = 'purchase.order.to.vendor.price.wizard'
    _rec_name = 'order_id'

    @api.multi
    def set_prices(self):
        self.ensure_one()
        supplierinfo_model = self.env['product.supplierinfo']

        msg = ''
        created = []
        updated = []

        for line in self.order_line_ids:
            # Check if a supplierinfo row exists for the vendor + product
            # combination
            args = [('product_tmpl_id', '=',
                     line.product_id.product_tmpl_id.id),
                    ('name', '=', self.partner_id.id),
                    ('type', '=', 'supplier')]

            # In special cases where the same product has multiple supplier
            # info lines for the same vendor, update only the first
            existing = supplierinfo_model.search(args=args, limit=1)

            if existing:
                existing[0].price = line.price_unit
                updated.append(line.product_id.name)
            else:
                seq = max(line.product_id.seller_ids.mapped('sequence')) + 1 \
                    if line.product_id.seller_ids else 1

                supplierinfo_model.create({
                    'product_tmpl_id': line.product_id.product_tmpl_id.id,
                    'name': self.partner_id.id,
                    'price': line.price_unit,
                    'sequence': seq,
                })
                created.append(line.product_id.name)

        if created:
            msg += _('Added vendor prices for %s for products:<br/>') \
                % self.partner_id.name
            msg += '<br/>'.join(created)
        if updated:
            if created:
                msg += '<br/><br/>'
            msg += _('Updated vendor prices for %s for products:<br/>') \
                % self.partner_id.name
            msg += '<br/>'.join(updated)

        if created or updated:
            self.order_id.message_post(
                body=msg,
                subtype='mt_comment',
            )

    order_id = fields.Many2one(
        comodel_name='purchase.order',
        string='Purchase Order'
    )

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Vendor',
        readonly=True,
    )

    order_line_ids = fields.Many2many(
        comodel_name='purchase.order.line',
        string='Order Lines',
    )
