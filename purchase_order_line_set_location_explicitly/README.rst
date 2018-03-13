.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================
Set PO Line Location Explicitly
===============================

* When confirming a Purchase Order, any lines without a set destination location
  are explicitly set to target the default location, i.e. the default destination
  of the selected picking type
* Intended to be used with OCA's purchase_location_by_line that advises against
  using a location structure where PO lines contain locations that are children
  of the default location of the purchase order's picking type (e.g. 
  WH > Stock > Sublocation and WH > Stock, respectively
* Setting the location explicitly on lines before order confirmation fixes the
  probles with delivery splitting into wrong number of picking in the 
  purchase_location_split_by_date module


Configuration
=============
* Install the OCA prerequisites purchase_location_by_line and
  purchase_location_split_by_date

Usage
=====
* Confirm a PO that has a line without a destination location set. The location
  gets set automatically.

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
