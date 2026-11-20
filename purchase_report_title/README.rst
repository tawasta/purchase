.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========================
Purchase Order Report Title
===========================
* Replaces the default titles of the Purchase Order and Request for Quotation
  prints with PURCHASE ORDER and REQUEST FOR QUOTATION.
* The titles can be changed per company in the purchase settings. An empty
  setting uses the default title.

Configuration
=============
* Go to Purchase > Configuration > Settings > Purchase Order Reports.
* Set Purchase Order Report Title and RFQ Report Title, and their translations.
  The print uses the language of the vendor.
* Leave a field empty to use the default title.

Usage
=====
Print a Purchase Order or a Request for Quotation.

The title settings were previously in a separate module that is now merged
into this one. On a database where that module is installed, updating this
module removes it and keeps the titles already set.

The settings fields are created when the server restarts, so a deployment that
restarts the server before updating the module keeps working until the update.
The update is still needed to bring the settings and the title changes into
use.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Timo Kekäläinen <timo.kekalainen@futural.fi>
* Miika Nissi <miika.nissi@futural.fi>
* Joonas Lahtinen <joonas.lahtinen@futural.fi>
* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
