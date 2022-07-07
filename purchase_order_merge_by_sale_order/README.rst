.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================================================
Create Purchase Order and merge it by Sale Order info
=====================================================

Normally Odoo merges purchase orders based mainly by its
Vendor. This is all well and good, unless purchase orders
are not wanted to be merged between Vendors. Installing this
module changes this process for future purchase orders which
are created from sale orders.

For example SO001 could contain these order lines:
- Product A, qty 1
- Product B, qty 3
- Product B, qty 2

With Make to Order and Buy routes set for these products and
assuming the Vendor is also the same, confirming SO001 will
create a purchase order with these lines:
- Product A, qty 1
- Product B, qty 5

What is different here is that other purchase orders won't
be merged to this order, but they are all separate orders.

A created purchase order will have a sale order record
attached to it.

Configuration
=============
\-

Usage
=====
* Install the module from Apps

Known issues / Roadmap
======================
\-

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
