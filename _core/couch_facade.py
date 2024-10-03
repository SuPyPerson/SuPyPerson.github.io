""" Façade to forward request to a remote base.

Classes neste módulo:
    - :py:class:`ScriptVito` include Vitollino scenes in the programming.
    - :py:func:`show` Called when dojo window is opened.
    - :py:func:`build` Called to collect scripts from side script file.
    - :py:class:`ScripStErr` Error Handler Class.
    - :py:class:`ScriptBuilder` Collect scripts from side script file.
    - :py:class:`ScriptWidget` Display Dojo elements in a window.

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

    def get(self, code):
        # codes = self.db.find({'selector': {"code_name__": {"$eq": f"{code}"}}}, fields=["code_name__"])
        codes = self.db.find(qy)
        # codes = self.db.get("20241003192045")
        # coded = [entry for entry in codes['docs']]
        print("RequestSender.get", code, codes['docs'], codes["warning"])
        # print("RequestSender.get", code, codes)
        return codes if codes else None
        # return list(codes)[0] if codes else None

    def save(self, code):
        code.update(_id=datetime.now().strftime("%Y%m%d%H%M%S%f"))
        value = self.db.save(dict(code))
        print("RequestSender.save", dict(code), value)
        return f"RequestSender.saved: {value}"
arguments = [env[f"{arg}_DB"] if f"{arg}_DB" in env else "" for arg in "USERNAME PASSWORD SERVER_URL DATABASE".split()]
MF = RequestSender(*arguments)
qy_ = {
   "selector": {
      r"code_name__": r"arco/forest_0.py/al0"

   }
}
qy = {
   "selector": {
      r"code_name__": r"arco forest_0.py al0"

   }
}
