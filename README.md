[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Pipeline Status](https://gitlab.com/tawasta/odoo/purchase/badges/17.0-dev/pipeline.svg)](https://gitlab.com/tawasta/odoo/purchase/-/pipelines/)

Purchase
========
Purchase Addons for Odoo.

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[purchase_auditlog_rules](purchase_auditlog_rules/) | 17.0.1.0.0 |  | Adds auditlog rules for Purchase
[purchase_order_additional_terms](purchase_order_additional_terms/) | 17.0.1.0.0 |  | Enables describing additional terms for a PO and adds them to PDF
[purchase_order_analytic_account](purchase_order_analytic_account/) | 17.0.1.0.2 |  | New field for indicating what AA the PO is related to
[purchase_order_carrier_id](purchase_order_carrier_id/) | 17.0.1.0.0 |  | Enables setting the carrier for a PO
[purchase_order_check_stock_availability](purchase_order_check_stock_availability/) | 17.0.1.0.0 |  | Trigger internal transfers from Purchase Order view
[purchase_order_contact_person](purchase_order_contact_person/) | 17.0.1.0.1 |  | Enables setting the vendor's contact person for a PO
[purchase_order_description](purchase_order_description/) | 17.0.1.0.0 |  | Adds a description (an internal note) to purchase order
[purchase_order_end_customer](purchase_order_end_customer/) | 17.0.1.0 |  | New field for storing the end customer of a PO
[purchase_order_expected_arrival_changes_picking_date](purchase_order_expected_arrival_changes_picking_date/) | 17.0.1.0.0 |  | Picking Scheduled date is changed by Expected Arrival
[purchase_order_header_text](purchase_order_header_text/) | 17.0.1.0.0 |  | New field for PO header/title and report configured in settings
[purchase_order_internal_reference](purchase_order_internal_reference/) | 17.0.1.0.1 |  | New field for storing an internal reference to PO
[purchase_order_latest_effective_date](purchase_order_latest_effective_date/) | 17.0.1.0.0 |  | Adds latest expected date to purchase orders from their lines
[purchase_order_line_forecasted_available](purchase_order_line_forecasted_available/) | 17.0.1.0.0 |  | Add virtual_available field on purchase order line
[purchase_order_line_location_from_analytic](purchase_order_line_location_from_analytic/) | 17.0.1.0.0 |  | Suggest line destination based on line's AA
[purchase_order_line_qty_available](purchase_order_line_qty_available/) | 17.0.1.0.0 |  | Add qty_available to purchase order line
[purchase_order_line_responsible](purchase_order_line_responsible/) | 17.0.1.0.0 |  | Product Responsible on Purchase order line
[purchase_order_line_use_standard_price](purchase_order_line_use_standard_price/) | 17.0.1.0.0 |  | Use standard price as line price, if no supplier price is set
[purchase_order_line_view](purchase_order_line_view/) | 17.0.1.0.0 |  | New view for inspecting PO lines
[purchase_order_mandatory_vendor_reference](purchase_order_mandatory_vendor_reference/) | 17.0.1.0.0 |  | Require a vendor reference before confirming a PO
[purchase_order_print_button_prints_po](purchase_order_print_button_prints_po/) | 17.0.1.0.0 |  | Replace the 'Print RFQ' Button with a 'Print PO' Button
[purchase_order_receive_service_product_qty](purchase_order_receive_service_product_qty/) | 17.0.1.0.0 |  | Receive service on confirmation of an order
[purchase_order_report_template](purchase_order_report_template/) | 17.0.1.0.0 |  | Minor fixes for Purchase Order Report
[purchase_order_requested_receipt_date](purchase_order_requested_receipt_date/) | 17.0.1.0.0 |  | Storing the delivery date requested from supplier
[purchase_order_select_tax](purchase_order_select_tax/) | 17.0.1.0.0 |  | Select tax from dropopwn-menu for Purchase Order Lines
[purchase_order_show_dropship_address](purchase_order_show_dropship_address/) | 17.0.1.0.0 |  | Show the full address below the Drop Ship Address
[purchase_order_standard_clause](purchase_order_standard_clause/) | 17.0.1.0.0 |  | Company-specific standard clause for POs
[purchase_order_tags](purchase_order_tags/) | 17.0.1.0.0 |  | Enables tagging purchase orders with keywords
[purchase_report_align_header_fields](purchase_report_align_header_fields/) | 17.0.1.0.0 |  | Align Purchase report Header fields
[purchase_report_approval_date](purchase_report_approval_date/) | 17.0.1.0.0 |  | Adds Approval Date to Purchase Reports
[purchase_report_business_code](purchase_report_business_code/) | 17.0.1.0.0 |  | QWeb purchase reports business code
[purchase_report_client_order_ref](purchase_report_client_order_ref/) | 17.0.1.0.0 |  | Add client order ref to purchase report
[purchase_report_date_only](purchase_report_date_only/) | 17.0.1.0.0 |  | Format Date to only show date without time in PO report
[purchase_report_hide_date_req](purchase_report_hide_date_req/) | 17.0.1.0.0 |  | Hides Date req on purchase order report
[purchase_report_hide_deadline](purchase_report_hide_deadline/) | 17.0.1.0.0 |  | Purchase Report Hide Deadline
[purchase_report_hide_phonenumber](purchase_report_hide_phonenumber/) | 17.0.1.0.0 |  | Hide Phonenumber on Purchase Reports
[purchase_report_hide_representative](purchase_report_hide_representative/) | 17.0.1.0.0 |  | Hides Purchase Representative on purchase report
[purchase_report_incoterm_name](purchase_report_incoterm_name/) | 17.0.1.0.0 |  | Show Incoterm name instead of code on Purchase Report
[purchase_report_incoterms](purchase_report_incoterms/) | 17.0.1.0.0 |  | QWeb purchase reports Incoterms
[purchase_report_order_reference](purchase_report_order_reference/) | 17.0.1.0.0 |  | Add PO order reference to header informations
[purchase_report_orderlines](purchase_report_orderlines/) | 17.0.1.1.0 |  | Fixes orderlines in purchase report
[purchase_report_partner_ref](purchase_report_partner_ref/) | 17.0.1.0.0 |  | Adds Vendor Reference to RFQ Print
[purchase_report_payment_terms](purchase_report_payment_terms/) | 17.0.1.0.2 |  | QWeb purchase reports Payment Terms
[purchase_report_purchase_representative_phone](purchase_report_purchase_representative_phone/) | 17.0.1.0.0 |  | Adds Purchase Representative's Phone to PO Print
[purchase_report_purchaser](purchase_report_purchaser/) | 17.0.1.0.0 |  | Add purchaser information to purchase order report.
[purchase_report_quotation_informations_element](purchase_report_quotation_informations_element/) | 17.0.1.0.0 |  | Informations element to purchase quotation print
[purchase_report_quotation_purchase_representative_name_and_phone](purchase_report_quotation_purchase_representative_name_and_phone/) | 17.0.1.0.0 |  | Adds Purchase Representative's Name and Phone to RFQ Print
[purchase_report_requested_receipt_date](purchase_report_requested_receipt_date/) | 17.0.1.0.0 |  | Requested receipt date to Sale Report
[purchase_report_show_product_name](purchase_report_show_product_name/) | 17.0.1.0.0 |  | Always show product on PO print lines
[purchase_report_title](purchase_report_title/) | 17.0.1.0.2 |  | Replaces default titles with a better purchase report title
[purchase_report_vendor_title](purchase_report_vendor_title/) | 17.0.1.0.0 |  | Add title for purchase report vendor address info.
[purchase_request_analytic_account_location](purchase_request_analytic_account_location/) | 17.0.1.0.0 |  | Adds analytic account stock location to PR
[purchase_request_analytic_account_to_po](purchase_request_analytic_account_to_po/) | 17.0.1.0.0 |  | Assign Analytic Account from Purchase request to Purchase order
[purchase_request_check_stock_availability](purchase_request_check_stock_availability/) | 17.0.2.3.1 |  | Trigger internal transfers from Purchase Request view
[purchase_request_from_bom_contents](purchase_request_from_bom_contents/) | 17.0.1.0.0 |  | Add BOM contents to PR lines
[purchase_request_from_bom_contents_analytic](purchase_request_from_bom_contents_analytic/) | 17.0.1.0.0 |  | Analytic Account Support for BOM to PR additions
[purchase_request_line_enable_approved_deletion](purchase_request_line_enable_approved_deletion/) | 17.0.1.0.0 |  | Allow deletion of Purchase request lines in approved-state
[purchase_request_line_show_purchases](purchase_request_line_show_purchases/) | 17.0.1.0.0 |  | Show related purchase orders' numbers
[purchase_request_make_po_currency](purchase_request_make_po_currency/) | 17.0.1.0.0 |  | Set a currency from a vendor to a new PO which is created from purchase request lines
[purchase_request_newest_first](purchase_request_newest_first/) | 17.0.1.0.0 |  | Shows newest Purchase Request lines first
[purchase_request_primary_vendor_info](purchase_request_primary_vendor_info/) | 17.0.1.0.0 |  | Helper fields for showing primary vendor's info

[//]: # (end addons)
