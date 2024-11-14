""" Façade to forward request to a remote base.

Classes neste módulo:
    - :py:class:`RequestSender` Send ajax requests to server.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    24.11
   |br| Decrypt token (12).

.. versionadded::    24.10
   |br| Initial version (03).
   |br| Working version (04).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
import json
from datetime import datetime as dt

from browser import ajax, alert
from base64 import encodebytes as ecd
from base64 import b64encode as ecd
# FOX = "the quick brown fox jumps over the lazy dog".replace(" ", "_")
# PYJ = "Wrt0j9osNgcZlXSY4dS@CGkhneBhNd5fb8E5YJcf9Ubyx_nG4YwBmD_McI2y_IaETRsPgLAP8ovZedXHzBhX_KpseYVGq"
PYJ = "tYmrYYO72SIPCIyu0M4W7P31T@xnwJo_IdFzzlMxvOJXKE6QjY2vtzS1KGfMoVbdDBZOwstd"
GHU = "github@pat@11ABCK4WQ0".replace("@", "_")
ERASE = None

class RequestSender:
    _instance = None
    _passwd = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RequestSender, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, passwd=None):
        self.result = ""
        self.user = "carlotolla"
        self.repo = "pyjr"
        self.getter = lambda *_: None
        self.passwd = RequestSender._passwd if RequestSender._passwd is not None else input("digite a senha")
        RequestSender._passwd = self.passwd

    def _decrypt(self, msg=PYJ):
        tp = self.passwd*20
        blk = ord("0")
        roll = "".join(chr(r) for r in range(blk, ord("z")+1) if chr(r) not in r':;<=>?[\]^`!"'+"#$%&'()*+,-./'")
        tape = [roll.index(p) for p in tp]
        # lor = roll[::-1]
        "".join(chr((roll.index(r)+t)) for r, t in zip(msg, tape))
        # msg = "".join(lor[(roll.index(r) - t)] for r, t in zip(msg, tape))
        # print(">>", msg)
        return GHU + "".join(roll[-(roll.index(r)-t+1)] for r, t in zip(msg, tape))

    def _save(self, content, path="pet/main.py", msg=None, sha=None, token=ERASE):
        msg = msg or "SuperPython Jogos"
        owner = self.user
        repo = self.repo
        # content = ecd(str.encode(content))
        content = ecd(content.encode()).decode()
        # content = ecd(str.encode(content) + b'==').encode("utf-8")
        token = token or self._decrypt()
        header = {"Accept": "application/vnd.github+json",
                  "Authorization": f"Bearer {token}",
                  "X-GitHub-Api-Version": "2022-11-28"}
        data = {"message": f"{msg}",
                "committer": {"name": "SuperPython Jogos", "email": "labasence@gmail.com"},
                "content": f"{content}"}
        data.update({"sha": sha}) if sha is not None else None
        data = json.dumps(data)
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        return header, url, data

    def save(self, code, data, sha=None, hook=None):
        msg = f"Pynoplia-{code} @{dt.now().strftime('%Y-%m-%d %H:%M:%S')}"
        header, url, data = self._save(data, path=code, msg=msg, sha=sha)
        # print("save w sha header url", header, url)
        req = ajax.Ajax()
        req.bind('complete', hook or self.on_complete)
        # send a POST request to the url
        req.open('PUT', url, True)
        [req.set_header(key, value) for key, value in header.items()]
        # send data as a dictionary
        req.send(data)

    def raw_get(self, path, getter):
        from urllib.request import urlopen
        owner, repo = self.user, self.repo
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/refs/heads/main/{path}"
        content = urlopen(url).read()
        getter(content)

    def get(self, code, getter):
        self.getter = getter
        self.code = code
        header, url, data = self._save("", path=code)
        # ajax.get(f"get_code/get/{self.user}/{code}", oncomplete=self.read)
        req = ajax.Ajax()
        req.bind('complete', self.read)
        # send a GET request to the url
        req.open('GET', url, True)
        [req.set_header(key, value) for key, value in header.items()]
        # req.set_header('content-type', 'application/x-www-form-urlencoded')
        # send data as a dictionary
        req.send()

    def read(self, code):
        self.result = code.read()
        # print(f"get_code/get/{self.result}")
        self.getter(json.loads(self.result))

    def on_complete(self, msg):
        _ = self
        tag = json.loads(msg.read())
        tag = tag["content"]["path"] if "content" in tag else "Falhou ao salvar"
        alert(f"Resultado da Operação: {self.code}: {tag}")


MF = RequestSender
if __name__ == '__main__':
    # print(RequestSender()._decrypt("".join(chr(r) for r in range(ord("a"), ord("z")+1))))
    print(RequestSender()._decrypt())
