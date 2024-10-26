""""Configure Docsify from Brython.

Classes neste módulo:
    - :py:class:`PaneEditor` Tabbed Pane.
    - :py:class:`Pane` A single pane with its tab.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    24.10
   |br| Classes PaneEditor, Pane (26).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from browser import window, document, alert, html, timer


class Head:
    """Add all stuff to head section"""
    STLIB = (f"/_core/css/{st}.css" for st in
             "editor lecture fa6.6.all.min darcula mermaid.min darcula.min prism-funky.min".split())
    HEAD = document.head
    J1 = "ace1.36.2.min mode1.36.2-python.min.js theme-1.36.2gruvbox.min ext1.36.2-language_tools.min mermaid.min"
    J1 += "ga.min docsify.min accordion.index external-script.min prism-python.min docsify-sidebar-collapse.min"
    SCT = (f"/_lib/{st}.js" for st in J1.split())

    def __init__(self, ln=html.LINK, st=html.SCRIPT):
        def append(child, node=self.HEAD):
            _ = node <= child
        [append(ln(rel="stylesheet", href=hr)) for hr in self.STLIB]
        [append(st(type="text/javascript", src=hr)) for hr in self.SCT]


def main():
    Head()


if __name__ == '__main__':
    main()
