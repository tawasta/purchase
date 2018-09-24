.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

========================================
Update Vendor Prices from Purchase Order
========================================

* Adds the possibility to batch update products' vendor prices from Purchase
  Order, based on the prices set on PO lines
* Intended as a shortcut for quickly update products' purchase prices

Configuration
=============
\-

Usage
=====
* Open a Purchase Order and click the "Set Vendor Prices" button
* Select the lines whose price should be updated. If an existing price is 
  found for the vendor of the PO, the price is updated. Otherwise a new
  supplierinfo row is created.

Known issues / Roadmap
======================
* Created for a single-UoM environment where no variants are used. If 
  variants or multiple UoMs are used, the module needs to be adjusted.

Credits
=======

Contributors
------------
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
