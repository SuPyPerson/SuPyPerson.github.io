""" Façade to forward request to a remote base.

Classes neste módulo:
    - :py:class:`RequestSender` Send ajax requests to server.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    24.10
   |br| Initial version (03).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from datetime import datetime as dt

from browser import ajax


class RequestSender:
    def __init__(self):
        self.result = ""
        self.user = "arco"

    def save(self, code, data):
        # ajax.post(f"get_code/save/{self.user}/{code}", oncomplete=self.read)
        req = ajax.Ajax()
        req.bind('complete', self.on_complete)
        # send a POST request to the url
        req.open('POST', f"get_code/save/{self.user}/{code}", True)
        req.set_header('content-type', 'application/x-www-form-urlencoded')
        # send data as a dictionary
        msg = f"{self.user}-{code} @{dt.now().strftime('%Y-%m-%d %H:%M:%S')}"
        req.send({'message__': msg, 'code_name__': f"{self.user}/{code}", 'code_data__': data})


    def get(self, code):
        ajax.get(f"get_code/get/{self.user}/{code}", oncomplete=self.read)

    def read(self, code):
        self.result = code
        print(code.read())

    def on_complete(self, msg):
        print(msg.read())


MF = RequestSender()
