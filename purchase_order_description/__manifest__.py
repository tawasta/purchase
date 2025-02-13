##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2017- Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
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
    "name": "Purchase Order Description",
    "summary": "Adds a description (an internal note) to purchase order",
    "version": "17.0.1.0.0",
    "category": "Purchase",
    "website": "https://github.com/tawasta/purchase",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["purchase"],
    "data": ["views/purchase_order.xml"],
}
