from odoo import fields, models


class PurchaseTag(models.Model):
    _name = "purchase_tags.tag"

    name = fields.Char(required=True)

    color = fields.Integer(string="Color Index")

    _sql_constraints = [
        ("name_uniq", "unique (name)", "Tag name already exists!"),
    ]
