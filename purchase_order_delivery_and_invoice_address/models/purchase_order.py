from odoo import fields, models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    po_invoice_address_id = fields.Many2one(
        string="Invoice Address", comodel_name="res.partner", copy=False
    )

    po_delivery_address_id = fields.Many2one(
        string="Delivery Address", comodel_name="res.partner", copy=False
    )

    show_invoice_and_delivery_address = fields.Boolean(
        string="Show Invoice and Delivery address",
        default=False,
        store=True,
        copy=False,
    )
