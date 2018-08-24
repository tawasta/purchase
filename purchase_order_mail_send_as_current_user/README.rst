.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==========================================
Purchase orders - use current user's email
==========================================

* By default Odoo uses the Purchase Order creator's e-mail address in the 
  'from' field when sending RFQs or POs to supplier using the core templates
* This can be problematic when e.g. reordering rules have triggered the PO
  creation as the admin user
* This module clears the 'from' field from the core e-mail templates 
  "Purchase Order - Send by Email" and "RFQ - Send by Email" so that the e-mail
  address of the person who triggers the e-mail sending gets used

Configuration
=============
* The template modifications use the noupdate flag, so you can still further
  customize them in the UI if needed.

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
