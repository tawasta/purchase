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
* The module includes a migration script to update project_id field by its related
  project.project record if this module has been used in 17 version. In this version
  project_id field used account.analytic.account model.

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
