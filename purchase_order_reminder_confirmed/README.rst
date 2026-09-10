.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

========================================
Purchase Order Reminder Confirmed Column
========================================

This module makes the vendor receipt reminder confirmation visible in the
purchase order list views.

Odoo can send vendors a reminder email before the promised receipt date
and record whether the vendor confirmed it. That confirmation status
already exists on the purchase order but is normally only visible on the
order form. This module adds it as a column in the Requests for
Quotation and Purchase Orders list views as well.

Configuration
=============
\-

Usage
=====

#. Open **Purchases > Orders > Requests for Quotation** or **Purchases
   > Orders > Purchase Orders**.
#. The **Reminder Confirmed** column shows whether the vendor has
   confirmed the receipt reminder for each order.
#. If the column is not shown, add it through the list view's optional
   columns toggle.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------
* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
