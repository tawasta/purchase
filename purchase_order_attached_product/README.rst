.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==============================
Attached products in purchases
==============================
* Adds a product's attached products to RFQs automatically, with the same
  unit (if allowed on the attached product) and quantity as the main line
* Based on the earlier work done by OCA/Tecnativa in the sale counterpart module,
  see https://github.com/OCA/sale-workflow/tree/17.0/sale_attached_product

Configuration
=============
* Configure attached products in Product form view > Attached Purchase Products
* Optional: create system parameter
  ``purchase_order_attached_product.auto_update_attached_lines`` with value
  ``True`` to keep attached lines in sync with their main line when e.g. 
  quantity or UoM changes.

Usage
=====
* Add a product with attached products to an RFQ and save
* Confirmed, cancelled and locked orders are not changed

Known issues / Roadmap
======================
* This module has been developed for a specific use case where bottle/can 
  deposit products are added to PO lines along with the actual bottles/cans.
  If you're dealing with a system that uses `purchase_stock` and you want 
  to replenish the attached products with e.g. reordering rules, the 
  module will likely need additional work. 

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
