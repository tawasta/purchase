##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2018 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
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
    "name": "Purchase Request Stock Availability check",
    "summary": "Trigger internal transfers from Purchase Request view",
    "version": "17.0.2.3.1",
    "category": "Purchases",
    "website": "https://github.com/tawasta/purchase",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": [
        "purchase_request_analytic_account_location",
        "stock_location_excess_mark",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/config_settings.xml",
        "views/purchase_request.xml",
    ],
    "demo": [],
}
