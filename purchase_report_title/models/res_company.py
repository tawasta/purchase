from odoo import fields, models
from odoo.tools import SQL
from odoo.tools.sql import column_exists

REPORT_TITLE_FIELDS = ("purchase_order_report_title", "purchase_rfq_report_title")


class ResCompany(models.Model):
    _inherit = "res.company"

    purchase_order_report_title = fields.Char(
        default="",
        translate=True,
    )
    purchase_rfq_report_title = fields.Char(
        string="RFQ Report Title",
        default="",
        translate=True,
    )

    def _register_hook(self):
        """Create the report title columns when the server restarts.

        Deployments restart the server with the new code before the module
        is updated. Every request reads the company, so a missing column would
        break the whole database until the update. Remove this together with
        the fields, or the columns would be created again.
        """
        super()._register_hook()
        for field_name in REPORT_TITLE_FIELDS:
            if column_exists(self.env.cr, self._table, field_name):
                continue
            # IF NOT EXISTS: several workers may load the registry at once
            self.env.cr.execute(
                SQL(
                    "ALTER TABLE %s ADD COLUMN IF NOT EXISTS %s %s",
                    SQL.identifier(self._table),
                    SQL.identifier(field_name),
                    SQL(self._fields[field_name].column_type[1]),
                )
            )
