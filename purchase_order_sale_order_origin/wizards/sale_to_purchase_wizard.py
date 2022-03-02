##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2022- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class SaleToPurchaseWizard(models.TransientModel):
    # 1. Private attributes
    _inherit = "sale.to.purchase.wizard"

    def create_purchase(self, current_sale):
        purchase_order_model = self.env["purchase.order"]
        initial_values = {
            "partner_id": self.partner_id.id,
            "company_id": current_sale.company_id.id,
            "currency_id": current_sale.currency_id.id
            or self.env.company.currency_id.id,
            "picking_type_id": self.picking_type_id.id,
            "origin": current_sale.name,
            "sale_order_origin_id": current_sale.id,
            "payment_term_id": self.partner_id.property_supplier_payment_term_id.id,
        }

        if self.picking_type_id.default_location_dest_id.usage == "customer":
            # Dropshippping
            initial_values["dest_address_id"] = current_sale.partner_shipping_id.id

        updated_values = purchase_order_model.play_onchanges(
            initial_values, ["partner_id"]
        )

        return purchase_order_model.create(updated_values)
