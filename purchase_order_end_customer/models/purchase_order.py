from odoo import fields, models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    end_customer_id = fields.Many2one(
        comodel_name="res.partner",
        string="End customer",
        domain=[("is_customer", "=", True)],
        help="The end customer this purchase order is related to",
    )
