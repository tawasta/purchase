from odoo import _, models


class PurchaseOrderReportXlsx(models.AbstractModel):
    _name = "report.purchase_order_report_xlsx.purchase_order_xlsx"
    _description = "Purchase Order XLSX Report"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, objects):
        workbook.set_properties(
            {"comments": "Created with Python and XlsxWriter from Odoo 14.0"}
        )
        sheet = workbook.add_worksheet(_("Purchase Order - XLSX"))
        sheet.set_landscape()
        sheet.fit_to_pages(0, 0)
        sheet.set_zoom(80)

        # Some column sizes changed to match their title
        sheet.set_column(0, 0, 25)
        sheet.set_column(1, 1, 55)
        sheet.set_column(2, 3, 15)
        sheet.set_column(4, 4, 15)
        sheet.set_column(5, 5, 15)

        # Column styles
        title_style = workbook.add_format(
            {"bold": True, "bg_color": "#FFFFCC", "bottom": 1}
        )

        sheet_title = [
            _("Code"),
            _("Description"),
            _("Qty"),
            _("Unit Price"),
            _("Total Price"),
        ]

        sheet.set_row(0, None, None, {"collapsed": 1})
        sheet.write_row(0, 0, sheet_title, title_style)
        sheet.freeze_panes(1, 0)
        i = 1

        for o in objects:
            for line in o.order_line:
                sheet.write(i, 0, line.product_id.default_code or "")
                sheet.write(i, 1, line.name)
                sheet.write(i, 2, line.product_qty)
                sheet.write(i, 3, line.price_unit)
                sheet.write(i, 4, line.price_subtotal)

                i += 1
