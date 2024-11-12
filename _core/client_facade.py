""" Façade to forward request to a remote base.

Classes neste módulo:
    - :py:class:`RequestSender` Send ajax requests to server.

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
from datetime import datetime as dt

from browser import ajax, alert


class RequestSender:
    def __init__(self):
        self.result = ""
        self.user = "arco"
        self.getter = lambda *_: None
        self.passwd = "the quick brown fox jumps over the lazy dog"

    def _decrypt(self, msg="the quick brown fox jumps over the lazy dog"):
        tp = self.passwd*20
        blk = ord(" ")
        tape = [ord(p)-blk for p in tp]
        roll = "".join(chr(r) for r in range(blk, ord("z")+1))
        lor = "".join(chr(r) for r in range(ord("z"), blk-1, -1))
        lr = len(roll)
        "".join(chr((roll.index(r)+t)) for r, t in zip(msg, tape))
        "".join(lor[(roll.index(r) - t)] for r, t in zip(msg, tape))
        return "".join(roll[(roll.index(r)-t)] for r, t in zip(msg, tape))

    def _save(self, content, owner="carlotolla", repo="pyjr", path="main.py", msg=None, token=None):
        msg = msg or "SuperPython Jogos"
        header = {"Accept": "application/vnd.github+json",
                  "Authorization": f"Bearer {token}",
                  "X-GitHub-Api-Version": "2022-11-28"}
        data = {"message": f"{msg}",
                "committer": {"name": "SuperPython Jogos", "email": "labasence@gmail.com"},
                "content": f"{content}"}
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        return header, url, data

    def save(self, code, data):
        # ajax.post(f"get_code/save/{self.user}/{code}", oncomplete=self.read)
        msg = f"{self.user}-{code} @{dt.now().strftime('%Y-%m-%d %H:%M:%S')}"
        header, url, data = self._save(data, owner="carlotolla", repo="pyjr", path="main.py", msg=msg)
        req = ajax.Ajax()
        req.bind('complete', self.on_complete)
        # send a POST request to the url
        req.open('POST', url, True)
        [req.set_header(key, value) for key, value in header.items()]
        # req.set_header('content-type', 'application/x-www-form-urlencoded')
        # send data as a dictionary
        req.send(data)
        # req.send({'message__': msg, 'code_name__': f"{self.user}/{code}", 'code_data__': data})

    def get(self, code, getter):
        self.getter = getter
        ajax.get(f"get_code/get/{self.user}/{code}", oncomplete=self.read)

    def read(self, code):
        self.result = code.read()
        # print(f"get_code/get/{self.result}")
        self.getter(self.result)

    def on_complete(self, msg):
        _ = self
        alert(f"Resultado da Operação: {msg.read()}")


MF = RequestSender()
