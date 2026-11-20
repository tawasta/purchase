"""Take over the module that was merged into this one.

The report title settings used to be in a separate module. Its code is
removed, so on a database where it is installed its views would stay active
next to the ones of this module, and the module would stay installed without
code. The fields keep their columns and values: only the ownership of their
XML ids moves to this module.
"""

OLD_MODULE = "purchase_report_title_rename"
NEW_MODULE = "purchase_report_title"


def migrate(cr, version):
    # The update of this module marks the old one, which depends on it, to
    # upgrade before this script runs
    cr.execute(
        "SELECT 1 FROM ir_module_module "
        "WHERE name = %s AND state IN ('installed', 'to upgrade')",
        (OLD_MODULE,),
    )
    if not cr.rowcount:
        return

    # This module creates the same views again when it is loaded
    cr.execute(
        """
        DELETE FROM ir_ui_view
        WHERE id IN (
            SELECT res_id FROM ir_model_data
            WHERE module = %s AND model = 'ir.ui.view'
        )
        """,
        (OLD_MODULE,),
    )
    cr.execute(
        """
        UPDATE ir_model_data
        SET module = %s
        WHERE module = %s
        AND model = 'ir.model.fields'
        AND name NOT IN (SELECT name FROM ir_model_data WHERE module = %s)
        """,
        (NEW_MODULE, OLD_MODULE, NEW_MODULE),
    )
    cr.execute("DELETE FROM ir_model_data WHERE module = %s", (OLD_MODULE,))
    cr.execute(
        "UPDATE ir_module_module SET state = 'uninstalled', latest_version = NULL "
        "WHERE name = %s",
        (OLD_MODULE,),
    )
