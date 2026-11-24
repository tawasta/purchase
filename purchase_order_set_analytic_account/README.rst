.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=============================================
Set Analytic Account for Purchase Order Lines
=============================================

* Enables to mass update the lines' analytic accounts with a separate button when the order is in draft state
* The project of a purchase order is shown more clearly in the upper part of the form header

Configuration
=============
* The module project_purchase is installed together with this module, if it has not
  yet been installed.

Usage
=====
* Go to a purchase order and select a project for it. Then update purchase order lines
  by the chosen project.

Known issues / Roadmap
======================
::

    IMPORTANT IN 19 VERSION!!! project_purchase module messes up how project_id field
    uses its related model, changing it from account.analytic.account
    to project.project.

    A person doing a version update from 17 version to 19 version should
    use commands like these to set correct values to project_id
    field:
    ALTER TABLE purchase_order ADD COLUMN openupgrade_legacy_17_0_project_id;
    UPDATE purchase_order SET openupgrade_legacy_17_0_project_id = project_id;
    UPDATE purchase_order po
        SET project_id = pp.id
        FROM project_project pp
        WHERE
            pp.analytic_account_id = po.project_id;

    Doing this with a migration script is not a good way, unfortunately.

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@futural.fi>
* Timo Kekäläinen <timo.kekalainen@tawasta.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
