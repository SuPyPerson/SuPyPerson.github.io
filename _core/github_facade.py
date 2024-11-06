""" Façade to forward request to Github API.
OBS: Github is from pygithub package.

Classes neste módulo:
    - :py:class:`RequestSender` Send ajax requests to server.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    24.11
   |br| Initial version (06).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from datetime import datetime as dt

from browser import ajax, alert
from github import Github, Auth
from base64 import decodebytes as dcd
import os as op
import datetime
TIMESTAMP = '@{:%Y-%m-%d %H:%M}'

REMOTE_URL = "https://github.com/SuPyPackage/SuPyGirls.git"
TOKEN = dcd(str.encode(op.environ["PCT"])).decode("utf-8")
# str(dcd(str.encode(op.environ["IKW"])))
USERNAME = "carlotolla"


class RequestSender:
    def __init__(self):
        self.result = ""
        self.user = "alvo"
        self.getter = lambda *_: None
        auth = Auth.Token("access_token")
        g = Github(auth=auth)

        g.get_user("carlotolla")
        self.user = g.get_user("carlotolla")
        self.repo = None

    def get_file_branched(self, project, packager, moduler="main.py"):
        self.repo = self.user.get_repo(project)
        self.repo.get_branches()
        ref = self.repo.get_branch(packager).commit.sha
        return self.repo.get_contents("{}/{}".format(packager, moduler), ref)

    def get_file_contents(self, project, packager, moduler="main.py"):
        self.repo = self.user.get_repo(project)
        path = "{}/{}" if packager else "{}{}"
        print("get_file_contents ", project, path.format(packager, moduler))
        return self.repo.get_contents(path.format(packager, moduler))

    def create_file(self, project, filename, decoded_content, comment=None):
        timestamp = TIMESTAMP.format(datetime.datetime.now())
        comment = comment if comment else "Created {} {}".format(filename, timestamp)
        self.repo = self.user.get_repo(project)
        self.repo.create_file("/{}".format(filename), comment, decoded_content)
        return comment
    """
    def create_project(self, project):
        curl -i -H 'Authorization: token TOKEN' -d '{"name":"grete"}' https://api.github.com/user/repos
        timestamp = TIMESTAMP.format(datetime.datetime.now())
        comment = "Created {} at {}".format(project, timestamp)
        self.user.create_repo("/{}".format(project), comment)
        return comment
    """

    def save_file(self, project, filename, decoded_content, comment=None):
        timestamp = TIMESTAMP.format(datetime.datetime.now())
        comment = comment if comment else "Saved {} {}".format(filename, timestamp)
        self.repo = self.user.get_repo(project)
        file = self.repo.get_contents(filename)
        self.repo.update_file("/{}".format(filename), comment, decoded_content, file.sha)
        return comment


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
