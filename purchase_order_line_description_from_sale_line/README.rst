.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

====================================================================
Get Purchase order line description from its related sale order line
====================================================================

Decription -field in PO line gets its content from the related sale order line.
This happens when MTO and Buy routes are used together and a purchase order
is created automatically from a sale order.

Configuration
=============
MTO and Buy routes are needed to be used to create purchases from sales.

Usage
=====
Go to a sale order and write something in the Description -field of the
sale order line. Then confirm the sale order and see that the content
of the field are copied to the Description -field of a PO line.

Known issues / Roadmap
======================
None known

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
