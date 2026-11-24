from odoo.tools import sql


def migrate(cr, version):
    # Odoo 19 replaced purchase.order.mail_reminder_confirmed with acknowledged.
    # The old column still exists here: it is dropped only after all modules
    # are loaded.
    if not sql.column_exists(cr, "purchase_order", "mail_reminder_confirmed"):
        return

    cr.execute(
        """
        UPDATE purchase_order
        SET acknowledged = TRUE
        WHERE mail_reminder_confirmed IS TRUE
          AND acknowledged IS NOT TRUE
        """
    )
