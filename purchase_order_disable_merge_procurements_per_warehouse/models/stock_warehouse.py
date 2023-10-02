from odoo import fields, models


class StockWarehouse(models.Model):

    _inherit = "stock.warehouse"

    # Allow only admins to use this field to avoid bad user cases
    never_merge_procurements = fields.Boolean(
        string="Disable procurements merge", groups="base.group_system"
    )
