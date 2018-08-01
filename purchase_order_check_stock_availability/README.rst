.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=======================================
Purchase Order Stock Availability check
=======================================

Purchase Orders have a button for checking the availability of requested
products in other stock locations. Internal transfers can be created instead 
of creating a purchase order.


Configuration
=============
\-

Usage
=====
* Click the "Check stock availability" button on the Purchase Order form
* "Products available in other stock locations" tab will now contain a list of 
  products available elsewhere
* Each line contains a "Transfer" button that can be used to create an Internal
  transfer from the product's current location to the location defined on the 
  purchase order.
* Clicking the transfer button will either a) remove the related purchase order
  line, if the whole required amount was available, or b) subtract the amount
  from the purchase order line, if it was only partially available in the
  other stock location.


Known issues / Roadmap
======================
* Note that the stock availability check is a manual process, the available
  stock quantities do not refresh automatically.
* This module is work in progress
* TODO: Unit of measure conversion handling

Credits
=======

Contributors
------------

* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
