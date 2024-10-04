""" Façade to forward request to a remote base.

Classes neste módulo:
    - :py:class:`RequestSender` Interacts with the couchdb module.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    24.10
   |br| Initial version (03).
   |br| Working version (04).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from datetime import datetime
from os import environ as env
from couchdb3 import Server


class RequestSender:
    def __init__(self, login="", password="", server_url="", database="", timeout=10):
        server = f"http://{login}:{password}@{server_url}" if login else f"http://{server_url}"
        print(server)
        db = Server(server)
        self.db = db.get(database or "pyjr")
        print(self.db)
        self.result = ""

    def get(self, name):
        name = name.replace(r"/", r"-")
        query = dict(selector=dict(code_name__=name), use_index="cadf8e8443131c88fff63125375b56fdf27c5a8e")
        codes = self.db.find(fields=["code_data__"], **query)
        code = codes["docs"][-1]["code_data__"] if ("docs" in codes) and (codes["docs"]) else None
        # print("RequestSender.get", name, code, codes["warning"] if "warning" in codes else None)
        return code

    def save(self, msg, name, data):
        name = name.replace(r"/", r"-")
        code = dict(_id=f"{name}-{datetime.now().strftime("%Y%m%d%H%M%S%f")}",
                    message__=msg, code_name__=name, code_data__=data)
        value = self.db.save(dict(code))
        # print("RequestSender.save", dict(code), value)
        return f"Arquivo salvo: {value}"


arguments = [env[f"{arg}_DB"] if f"{arg}_DB" in env else "" for arg in "USERNAME PASSWORD SERVER_URL DATABASE".split()]
MF = RequestSender(*arguments)
# https://horacio.selfip.org:5984/_utils
