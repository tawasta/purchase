from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    tag_ids = fields.Many2many(comodel_name="purchase_tags.tag", string="Tags")
