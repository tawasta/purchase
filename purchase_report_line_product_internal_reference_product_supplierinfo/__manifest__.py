##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2025- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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
    "name": "Purchase Order reports - Product's internal reference / Supplier Code integration",
    "summary": "Conditional showing of own + supplier product code and name on prints",
    "version": "17.0.1.0.0",
    "category": "Reporting",
    "website": "https://github.com/tawasta/purchase",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["purchase_report_line_product_internal_reference"],
    "data": [
        "report/purchase_order_report.xml",
        "report/request_for_quotation_report.xml",
    ],
}
