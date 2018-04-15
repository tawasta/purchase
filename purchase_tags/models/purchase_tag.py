# -*- coding: utf-8 -*-
from odoo import models, fields


class PurchaseTag(models.Model):

    _name = "purchase_tags.tag"

    name = fields.Char(
        string='Name',
        required=True
    )

    color = fields.Integer(
        string='Color Index'
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists!"),
    ]
