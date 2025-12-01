.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=======================================
Purchase Request status change messages
=======================================

::

    Adds a functionality to send messages when a user requests an approval for
    a purchase request. Then a message (e-mail) is sent to the approver with
    a link to the purchase request.

    Approving a purchase request sends a message to the e-mail address of company
    assigned to a purchase request. The message has the number of a purchase request
    and the name of approver.

    Rejecting a purchase request sends a message to the user in Requested By -field
    of a purchase request. This message also has a link to the purchase request.

Configuration
=============
::

    Check that the company used in purchase requests has an assigned e-mail address,
    because messages are sent to this address.

Usage
=====
::

    Select a purchase request and use these buttons to check how messages are sent:
    -Request approval
    -Approve
    -Reject

Known issues / Roadmap
======================
::

    Since sending messages is an added feature, there should not be any conflicts
    with other modules that use the same buttons as this module does.

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
