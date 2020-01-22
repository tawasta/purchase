.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================================================
New Purchase Orders are never linked to existing ones
=====================================================

When a new purchase order is created, Procurement order uses a domain that is
based on multiple conditions. This module adds a condition that is never true
in this domain, resulting in that a new purchase order is always created.

Configuration
=============
No special configuration needed.

Usage
=====
Install this module from Apps.

Known issues / Roadmap
======================
The more Sale orders are cancelled and confirmed again, the more likely it is
that unncessary Purchase orders will be created. It is advisable to use this
module only when cancelling and reconfirming Sale orders is rather rare in
given installation.

Credits
=======

Contributors
------------

* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>
* Timo Kekäläinen <timo.kekalainen@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
