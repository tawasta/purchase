# -*- coding: utf-8 -*-


import logging
import textwrap
from odoo.report import report_sxw
from odoo.tools.translate import _
from odoo.tools import html2plaintext

_logger = logging.getLogger(__name__)

try:
    from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
except ImportError:
    _logger.debug("report_xlsx not installed, Excel export non functional")

    class ReportXlsx(object):
        def __init(self, *args, **kwargs):
            pass

class VendorBillXlsx(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, objects):
        workbook.set_properties({
            'comments': 'Createed with Python and XlsxWriter from Odoo 10.0'})
        sheet = workbook.add_worksheet(_('Vendor bill'))
        sheet.set_landscape()
        sheet.set_zoom(60)
        sheet.fit_to_pages(1, 0)
        sheet.set_column(0, 0, 20)
        sheet.set_column(1, 1, 10)
        sheet.set_column(2, 4, 30)
        sheet.set_column(5, 5, 80)
        sheet.set_column(6, 6, 50)
        sheet.set_column(7, 11, 30)
        bold = workbook.add_format({'bold': True})
        title_style = workbook.add_format({'bold': True,
                                           'bg_color': '#CCE4FD',
                                           'bottom': 1})


        sheet_title = [_('Supplier'),
                    _('Reference'),
                    _('Invoice total (excluding VAT)'),
                    _('Invoice total (including VAT)'),
                    _('Project'),
                    _('Internal message'),
                    _('Description'),
                    _('Project dimension'),
                    _('Product group dimension'),
                    _('Project type dimension'),
                    _('Product type dimension'),
                    _('Bill Date'),
                    ]
        sheet.set_row(0, None, None, {'collapsed': 1})
        sheet.write_row(1, 0, sheet_title, title_style)
        sheet.freeze_panes

        message = ''

        ROW_H = 30

        i = 2
        for o in objects:
            message = ''
            ROW_H = 30
            j = 0
            msg_len = 0
            project_dimension = ''
            product_group_dimension = ''
            project_type_dimension = ''
            product_type_dimension = ''
            sheet.write(i, 0, o.partner_id.name or '', bold)
            sheet.write(i, 1, o.reference or '', bold)
            sheet.write(i, 2, o.amount_untaxed or 0, bold)
            sheet.write(i, 3, o.residual or 0, bold)
            sheet.write(i, 4, o.analytic_account_id.name or '', bold)
            for msg in o.message_ids:
                if msg.message_type == 'comment':
                    msg_len += 1
            for msg in o.message_ids:
                if msg.message_type == 'comment':
                    while j < msg_len:
                        ROW_H += 45
                        for x in range(1, 10):
                            if len(html2plaintext(msg.body)) > 70*x:
                                ROW_H += 10
                        if msg_len == 1:
                            message += _('Note by: ') + msg.author_id.name + \
                            '\n' + _('Date: ') + msg.date + '\n' + _('Comment: ') \
                            + '\n'.join(textwrap.wrap(html2plaintext(msg.body)))
                            break
                        j += 1
                        if j == msg_len:
                            message += _('Note by: ') + msg.author_id.name + '\n' \
                            + _('Date: ') + msg.date + '\n' + _('Comment: ') + \
                            '\n'.join(textwrap.wrap(html2plaintext(msg.body)))
                            break
                        else:
                            message += _('Note by: ') + msg.author_id.name + '\n' \
                            + _('Date: ') + msg.date + '\n' + _('Comment: ') + \
                            '\n'.join(textwrap.wrap(html2plaintext(msg.body))) + '\n' + 10*'-' + '\n'

            sheet.set_row(i, ROW_H, None)
            sheet.write(i, 5, message or '', bold)
            sheet.write(i, 6, o.description or '', bold)
            for tag in o.analytic_tag_ids:
                if tag.analytic_dimension_id.code == 'projektit':
                    project_dimension = tag.name
                if tag.analytic_dimension_id.code == 'tuoteryhmt':
                    product_group_dimension = tag.name
                if tag.analytic_dimension_id.code == 'projektilaji':
                    project_type_dimension = tag.name
                if tag.analytic_dimension_id.code == 'tuotelajit':
                    product_type_dimension = tag.name
            sheet.write(i, 7, project_dimension  or '', bold)
            sheet.write(i, 8, product_group_dimension or '', bold)
            sheet.write(i, 9, project_type_dimension or '', bold)
            sheet.write(i, 10, product_type_dimension or '', bold)
            sheet.write(i, 11, o.date_invoice or '', bold)
            i += 1

VendorBillXlsx('report.vendor.bill.xlsx', 'account.invoice',
                parser=report_sxw.rml_parse)

