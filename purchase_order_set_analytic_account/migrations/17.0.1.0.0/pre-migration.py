from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr,
        """ALTER TABLE purchase_order ADD COLUMN project_id_v14_analytic_account""",
    )
    # Just in case store the values to project_id_v14_analytic_account column
    openupgrade.logged_query(
        env.cr,
        """UPDATE purchase_order SET project_id_v14_analytic_account = project_id""",
    )

    # This updates purchase order project_id to be the same as the
    # project.project of purchase's analytic account. This is wrong
    # at first because it is the ID of project.project record. But
    # project_purchase module from v19 core has the same project_id
    # field and its model is project.project instead of account.analytic.account
    openupgrade.logged_query(
        env.cr,
        """UPDATE purchase_order po
            SET project_id = pp.id
            FROM project_project pp
            WHERE
                pp.analytic_account_id = po.project_id""",
    )
