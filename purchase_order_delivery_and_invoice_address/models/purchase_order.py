from odoo import fields, models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    po_invoice_address_id = fields.Many2one(
        string="Invoice Address", comodel_name="res.partner", copy=False
    )

    po_delivery_address_id = fields.Many2one(
        string="Delivery Address", comodel_name="res.partner", copy=False
    )

    other_invoice_and_delivery_address = fields.Boolean(
        string="Other Invoice and Delivery address",
        default=False,
        store=True,
        copy=False,
    )

    related_warehouse_partner_id = fields.Many2one(
        related="picking_type_id.warehouse_id.partner_id"
    )

    related_company_partner_id = fields.Many2one(related="company_id.partner_id")
