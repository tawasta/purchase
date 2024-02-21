from odoo import models


class PurchaseRequestLine(models.Model):
    _inherit = "purchase.request.line"
    _order = "request_id ASC,id ASC"
