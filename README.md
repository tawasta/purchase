[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Build Status](https://travis-ci.org/Tawasta/purchase.svg?branch=10.0)](https://travis-ci.org/Tawasta/purchase)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5533f4aeca2045459e731d58c9c324d4)](https://www.codacy.com/app/jarmokortetjarvi/purchase?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Tawasta/purchase&amp;utm_campaign=Badge_Grade)

Purchase-related addons
=======================

[//]: # (addons)

Available addons
----------------
addon | version | summary
--- | --- | ---
[purchase_menu_default_vendor_bills](purchase_menu_default_vendor_bills/) | 10.0.1.0.5 | Vendor bills as default (first) menu item
[purchase_order_actual_receipt_date](purchase_order_actual_receipt_date/) | 10.0.1.1.0 | Logs the date when all lines have been received
[purchase_order_additional_terms](purchase_order_additional_terms/) | 10.0.1.0.0 | Enables describing additional terms for a PO
[purchase_order_analytic_account](purchase_order_analytic_account/) | 10.0.1.1.0 | New field for indicating what AA the PO is related to
[purchase_order_analytic_account_to_notes](purchase_order_analytic_account_to_notes/) | 10.0.1.0.0 | Append analytic account to purchase notes on order validate
[purchase_order_buyer](purchase_order_buyer/) | 10.0.1.0.0 | Enables setting the buyer for a PO
[purchase_order_check_stock_availability](purchase_order_check_stock_availability/) | 10.0.1.1.0 | Trigger internal transfers from Purchase Order view
[purchase_order_confirmation_date](purchase_order_confirmation_date/) | 10.0.1.0.0 | Logs the date when the PO was confirmed
[purchase_order_contact_person](purchase_order_contact_person/) | 10.0.1.0.2 | Enables setting the vendor's contact person for a PO
[purchase_order_date_planned_auto_update](purchase_order_date_planned_auto_update/) | 10.0.1.0.0 | Automatically change the planned date for all order lines
[purchase_order_description](purchase_order_description/) | 10.0.0.1.0 | Adds a description (an internal note) to purchase order
[purchase_order_end_customer](purchase_order_end_customer/) | 10.0.1.1.0 | New field for storing the end customer of a PO
[purchase_order_internal_reference](purchase_order_internal_reference/) | 10.0.0.1.0 | New field for storing an internal reference to PO
[purchase_order_line_both_codes_in_description](purchase_order_line_both_codes_in_description/) | 10.0.1.0.0 | Show both codes in line description field
[purchase_order_line_location_from_analytic](purchase_order_line_location_from_analytic/) | 10.0.0.3.0 | Suggest line destination based on line's AA
[purchase_order_line_running_number](purchase_order_line_running_number/) | 10.0.1.0.0 | Simple running number for PO lines
[purchase_order_line_set_location_explicitly](purchase_order_line_set_location_explicitly/) | 10.0.1.0.0 | Confirming a PO sets lines' empty destination locations
[purchase_order_line_use_standard_price](purchase_order_line_use_standard_price/) | 10.0.1.0.0 | Use standard price as line price, if no supplier price is set
[purchase_order_line_view](purchase_order_line_view/) | 10.0.1.0.0 | New view for inspecting PO lines
[purchase_order_mail_send_as_current_user](purchase_order_mail_send_as_current_user/) | 10.0.1.0.0 | Send RFQs/POs from current user's address as default
[purchase_order_planned_date_in_header](purchase_order_planned_date_in_header/) | 10.0.1.0.1 | Move scheduled date from notebook tab to header
[purchase_order_requested_receipt_date](purchase_order_requested_receipt_date/) | 10.0.1.1.0 | Storing the delivery date requested from supplier
[purchase_order_set_product_prices_from_po](purchase_order_set_product_prices_from_po/) | 10.0.1.0.0 | Batch update products' cost prices from PO
[purchase_order_set_vendor_prices_from_po](purchase_order_set_vendor_prices_from_po/) | 10.0.1.0.1 | Batch update products' vendor prices from PO
[purchase_order_show_dropship_address](purchase_order_show_dropship_address/) | 10.0.1.0.0 | Show the full address below the Drop Ship Address
[purchase_order_standard_clause](purchase_order_standard_clause/) | 10.0.1.1.0 | Company-specific standard clause for POs
[purchase_order_to_sale_order](purchase_order_to_sale_order/) | 10.0.1.0.1 | Adds a wizard for creating a SO from PO and linking them
[purchase_order_tree_no_origin](purchase_order_tree_no_origin/) | 10.0.1.0.0 | Remove origin field from PO lists
[purchase_order_tree_partner_ref](purchase_order_tree_partner_ref/) | 10.0.1.0.0 | Show vendor reference field also in PO lists
[purchase_order_weight](purchase_order_weight/) | 10.0.1.2.0 | Add weight on PO and PO lines
[purchase_procurement_vendor_minimum_qty](purchase_procurement_vendor_minimum_qty/) | 10.0.1.0.0 | New POs from procurements attempt to respect vendor minimums
[purchase_product_analytic_tags](purchase_product_analytic_tags/) | 10.0.1.1.0 | Adds purchase order line analytic tags from products
[purchase_project_analytic_tags](purchase_project_analytic_tags/) | 10.0.1.1.0 | Adds purchase order line analytic tags from analytic account
[purchase_request_analytic_account](purchase_request_analytic_account/) | 10.0.1.1.0 | New field for indicating what AA the PR is related to
[purchase_request_analytic_account_location](purchase_request_analytic_account_location/) | 10.0.1.0.0 | Adds analytic account stock location to PR
[purchase_request_check_stock_availability](purchase_request_check_stock_availability/) | 10.0.1.0.1 | Trigger internal transfers from Purchase Request view
[purchase_request_from_bom_contents](purchase_request_from_bom_contents/) | 10.0.1.0.2 | Add BOM contents to PR lines
[purchase_request_from_bom_contents_analytic](purchase_request_from_bom_contents_analytic/) | 10.0.1.0.0 | Analytic Account Support for BOM to PR additions
[purchase_request_from_po_lines](purchase_request_from_po_lines/) | 10.0.1.0.0 | Create PRs from existing PO lines
[purchase_request_line_show_purchases](purchase_request_line_show_purchases/) | 10.0.1.0.0 | Show related purchase orders' numbers
[purchase_request_newest_first](purchase_request_newest_first/) | 10.0.1.0.0 | Shows newest Purchase Requests first
[purchase_request_primary_vendor_info](purchase_request_primary_vendor_info/) | 10.0.1.0.1 | Helper fields for showing primary vendor's info
[purchase_tags](purchase_tags/) | 10.0.1.0.0 | Enables tagging purchase orders with keywords
[res_partner_default_supplier_incoterm](res_partner_default_supplier_incoterm/) | 10.0.1.0.0 | Set a default incoterm for supplier

[//]: # (end addons)

