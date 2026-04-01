.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

============================================================
Set Shipping address to Purchase PDF print from Picking type
============================================================

::

    Select a shipping address in picking type. Purchases use Delivery To -field
    that is a picking type record. By defining a shipping address there it shows
    that address in purchase PDF prints, both PO and RFQ versions, if this picking
    type is selected to Delivery To -field.

Configuration
=============
::

    Define a shipping address to a picking type which is expected to be used
    on purchases.

Usage
=====
::

    Go to a purchase and select a picking type. Define a shipping address to this
    picking type if it does not have it already. Then print out a PDF print from
    this purchase.

Known issues / Roadmap
======================
::

    XML in this module slithly alters the conditions when Shipping Address is shown.
    But it should not disturb how the shipping address is normally shown on PDF print.

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
