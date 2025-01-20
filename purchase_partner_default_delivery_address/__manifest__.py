##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2025 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    "name": "Use default delivery address from Vendor in purchases",
    "summary": "Put default delivery address to a purchase from its vendor",
    "version": "14.0.1.0.1",
    "category": "Purchase Workflow",
    "website": "https://gitlab.com/tawasta/odoo/purchase",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "partner_default_delivery_address",
        "purchase_order_delivery_and_invoice_address",
    ],
    "data": [],
}
