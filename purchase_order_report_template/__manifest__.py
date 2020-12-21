##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2019- Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
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
    "name": "Purchase Order Report Template",
    "summary": "Purchase Order Report Template",
    "version": "12.0.1.0.0",
    "category": "Purchase",
    "website": "http://www.tawasta.fi",
    "author": "Tawasta",
    "license": "AGPL-3",
    "data": [
        "report/purchase_order_template.xml",
    ],
    "depends": [
        "purchase",
        "purchase_stock",
        "purchase_report_approval_date",
        "purchase_order_report_informations_element",
    ],
    "application": False,
    "installable": True,
}

