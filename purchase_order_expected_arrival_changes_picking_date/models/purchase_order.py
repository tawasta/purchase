from odoo import api, models
import logging

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange("date_planned")
    def onchange_date_planned(self):
        self_id = self._origin.id

        pickings = self.env["stock.picking"].search(
            [
                ("purchase_id", "=", self_id),
                ("state", "not in", ["done", "cancel"]),
            ]
        )

        if pickings:
            _logger.info(
                "Expected Arrival {} on {} changed scheduled date of its"
                " pickings {}".format(
                    self.date_planned, self.name, ", ".join([p.name for p in pickings])
                )
            )

        for picking in pickings:
            picking.po_date_planned = self.date_planned
            picking._compute_scheduled_date()

        return super().onchange_date_planned()
