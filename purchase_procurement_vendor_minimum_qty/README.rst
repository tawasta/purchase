.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==============================================
Vendor minimum order quantity for procurements
==============================================

New Purchase Orders from procurement orders attempt to respect vendor minimum quantities

* By default when a product has multiple vendors, the first one on the list is 
  suggested for a new purchase order originating from a procurement order
* With this module the procurement order tries to first find a vendor whose 
  minimum order quantity < required procurement quantity
* If no such vendor is found, the search falls back to Odoo core functionality 
  that suggests the vendor with the highest priority

Configuration
=============
\-

Usage
=====
\-

Known issues / Roadmap
======================
\-

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
