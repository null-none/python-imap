=======
Install
=======

.. code-block:: bash

    pip install python-imap


=======
Example
=======

.. code-block:: python

    from imap.client import ImapClient

    email = ''
    password = ''
    client = ImapClient(email, password)
    client.all()


=======
License
=======

MIT
