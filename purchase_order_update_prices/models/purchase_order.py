
from odoo import _, api, fields, models
from odoo.addons.queue_job.job import job
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrderLine(models.Model):

    _inherit = 'purchase.order.line'

    @api.multi
    @job
    def _cron_update_purchase_order_prices(self, lines):
        old_prices = lines.mapped('price_unit')
        for line in lines:
            if not line.product_id:
                continue

            params = {'order_id': line.order_id}
            seller = line.product_id._select_seller(
                 partner_id=line.partner_id,
                 quantity=line.product_qty,
                 date=line.order_id.date_order and line.order_id.date_order.date(),
                 uom_id=line.product_uom,
                 params=params)

            if not seller:
                if line.product_id.seller_ids.filtered(
                        lambda s: s.name.id == line.partner_id.id):
                    line.write({'price_unit': 0.0})
                continue

            price_unit = self.env['account.tax'].\
                _fix_tax_included_price_company(
                        seller.price, line.product_id.supplier_taxes_id,
                        line.taxes_id, line.company_id) if seller else 0.0

            if price_unit and seller and line.order_id.currency_id and \
                    seller.currency_id != line.order_id.currency_id:
                price_unit = seller.currency_id._convert(price_unit,
                        line.order_id.currency_id, line.order_id.company_id,
                        line.date_order or fields.Date.today())

            if seller and self.product_uom and \
                    seller.product_uom != self.product_uom:
                price_unit = seller.product_uom._compute_price(price_unit,
                        self.product_uom)

            line.write({'price_unit': price_unit})
        return 'Lines:', lines, 'New prices:', lines.mapped('price_unit'), \
               'Old prices:', old_prices

    @api.multi
    @job
    def cron_update_purchase_order_prices(self):
        """ Updates Purchase Order lines prices """

        lines = self.env['purchase.order.line'].search(
                [('state', '=', 'draft')])

        batch_lines = list()
        interval = 50
        for x in range(0, len(lines), interval):
            batch_lines.append(lines[x:x+interval])

        for batch in batch_lines:
            job_desc = _(
                "Assign prices to lines: {}".format(batch)
            )
            self.with_delay(
                description=job_desc)._cron_update_purchase_order_prices(batch)

        _logger.info("Cron Update Purchase Order prices completed")
