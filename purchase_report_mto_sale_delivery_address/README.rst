.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

========================================================
Related sale delivery address is shown on purchase print
========================================================

Purchases created from sales with MTO+Buy routes have original_sale_id information
thanks to purchase_order_merge_by_sale_order module. This original_sale_id field is
used to show delivery address from sale order on purchase order prints.

Configuration
=============
MTO (make to order) and Buy routes are needed to be used to properly to use
purchase_order_merge_by_sale_order module and show delivery address from sale
on purchase prints.

Usage
=====
Go to a purchase order which was created from sale and print the reports of the purchase

Known issues / Roadmap
======================
Other modules may change the prints of purchases

Credits
=======

Contributors
------------

* Timo Kekäläinen <timo.kekalainen@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
