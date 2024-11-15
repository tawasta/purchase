##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2022- Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
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
    "name": "Purchase Report HS Code",
    "summary": "Add HS code to purchase report lines",
    "version": "14.0.3.2.1",
    "category": "Reporting",
    "website": "https://gitlab.com/tawasta/odoo/purchase",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "purchase",
        "purchase_order_hs_code",
        "purchase_report_orderlines",
        "product_harmonized_system",
    ],
    "data": [
        "report/purchase_order_templates.xml",
        "views/purchase_order.xml",
        "views/res_config_settings.xml",
    ],
}
