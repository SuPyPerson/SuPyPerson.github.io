"""Game editor with github access.

Classes neste módulo:
    - :py:class:`ScriptWidget` Display Dojo elements in a window.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    24.08
   |br| Initial version (20).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from ScriptWidget import ScriptWidget, COD
import os

print(os.environ)
# print(os.environ['TOKEN'])
GIT = "https://raw.githubusercontent.com/carlotolla/pggames/master/pyjr/carlo/main.py"
ALF = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxy'
AFL = len(ALF)-1
TOK = "UUjcn_ZnZmYml35x7tNQ0dtAZXYVYJYSLRjU8eILKI75mQR8D31jPMaot8hV1nSmCpfIah9lpH9xZM5CKGtSORxusRXC1"


class Editor:
    def __init__(self, browser):
        self.browser = browser
        COD["pyedit"] = ""
        # COD[d["pyedit"]] = ""
        self.sw = ScriptWidget("Supy Editor", "pyedit",
                               alignment='left-right', height=500, show_scenario=False)  # .get_script()

    def get_scripts_callback(self, request):
        multi = request.text
        self.sw.editor.setValue(multi, -1)
        # print(multi, "\n", multi[0].split("  # _SEC_\n\n"))

    def get_script(self):
        req = self.browser.ajax.ajax()
        req.open('GET', GIT, True)
        req.set_header('content-type', "application/x-www-form-urlencoded;charset=UTF-8")
        req.bind('complete', self.get_scripts_callback)
        req.send()


def crypt(phrase, pay=TOK, enc=True):
    from hashlib import sha256 as sh
    shift = -1 if enc else 1
    phrase = sh(phrase.encode('ascii')).hexdigest() * 10
    return "".join([ALF[(ALF.index(s) + shift * int(f, base=16)) % AFL] for f, s in zip(phrase, pay)])


def main(browser):
    Editor(browser).get_script()
    # cy = crypt("")
    # dy = crypt("", pay=cy, enc=False)
    # print(cy, dy)


if __name__ == "__main__":
    pass  # main(None)
