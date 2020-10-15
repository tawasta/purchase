from odoo import models


class PurchaseRequest(models.Model):

    _inherit = "purchase.request"
    _order = "id DESC"
