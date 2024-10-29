""""Configure Docsify from Brython.

Classes neste módulo:
    - :py:class:`Head` Add all stuff to head section.
    - :py:function:`initial` Set DOM hooks.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    24.10
   |br| Classes Head, Pane (26).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http:#is.gd/3Udt>`_.
|   `Labase <http:#labase.selfip.org/>`_ - `NCE <https:#portal.nce.ufrj.br>`_ - `UFRJ <https:#ufrj.br/>`_.
"""
from browser import window, document, alert, html, timer


class Head:
    """Add all stuff to head section"""
    # SL = "editor lecture fa6.6.all.min darcula mermaid.min darcula.min prism-funky.min".split()
    SL = "fa6.6.all.min darcula darcula.min prism-funky.min accordion_style lecture editor".split()
    STLIB = (f"/_core/css/{st}.css" for st in SL)
    HEAD = document.head
    BODY = document.body
    J1 = "ace1.36.2.min mode1.36.2-python.min.js theme-1.36.2gruvbox.min ext1.36.2-language_tools.min mermaid.min"
    J2 = ("main_index external-script.min docsify.min ga.min accordion.index"
          " docsify-sidebar-collapse.min")
    SCT = (f"/_lib/{st}.js" for st in J1.split())
    SCB = (f"/_lib/{st}.js" for st in J2.split())

    def __init__(self, ln=html.LINK, st=html.SCRIPT):
        def append(child, node=self.HEAD):
            _ = node <= child

        window.docBasePath = "snct"
        [append(st(src=hr)) for hr in self.SCT]
        [append(ln(rel="stylesheet", href=hr)) for hr in self.STLIB]
        self.scripter()
        timer.set_timeout(self.pos_scripter, 100)

    def scripter(self, st=html.SCRIPT, *_):
        def append(child, node=self.HEAD):
            _ = node <= child
        # append(st("/_lib/main_index.js", self.BODY))
        # [append(st(type="text/javascript", src=hr)) for hr in self.SCT]
        [append(st(src=hr), self.BODY) for hr in self.SCB]

    def pos_scripter(self, st=html.SCRIPT, *_):
        def append(child, node=self.HEAD):
            _ = node <= child
        append(st(src="/_lib/prism-python.min.js"), self.BODY)
        # [append(st(type="text/javascript", src=hr)) for hr in self.SCT]
        # [append(st(src=hr), self.BODY) for hr in self.SCB]
        # [append(st(type="text/javascript", src=hr)) for hr in self.SCT]
        # [append(st(type="text/javascript", src=hr), self.BODY) for hr in self.SCB]


def initial():
    from browser import window, document, alert, html, timer
    from ScriptWidget import show, build, PLB
    import ScriptWidget as sw
    from browser.session_storage import storage

    def clipboard_show(bt):
        btp = bt.parent.previousSibling
        storage[PLB] = btp.text
        window.navigator.clipboard.writeText(btp.text)

    try:
        sw.SPR = window.__SP_RELEASE__
    except Exception as e:
        queryString = window.location.search
        urlParams = window.URLSearchParams.new(queryString)
        sw.SPR = urlParams.get('rel') or "@"
    print("urlParams.get('rel')", sw.SPR)

    window.__widget__ = show
    window.__did_got__ = build
    window.__copy_clip__ = clipboard_show


def docsy():
    ARGS = {

        "basePath": "snct",
        "coverpage": ["/", "/jaie24/"],
        "executeScript": False,
        "accordify": {
            "prerenderComments": True,
            "selectors": ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
            "debug": False
        },

        "alias": {
            '/pyi/(.*)': '/pgintro/$1',
            '/pintro': '/pgintro/README',
            '/kwa': '/kwarwp/README',
            '/pyjr/(.*)': '/pyjr/$1',
            '/jaie24': '/README',
            '/soho': '/kwarwp/o_sonho',
            '/jardim': '/sbce/o_jogo',
            '/changelog':
                'https:#raw.githubusercontent.com/docsifyjs/docsify/master/CHANGELOG',
            '/.*/_sidebar.md': '/_sidebar.md',
        },
        "name": 'Pynoplia',
        "nameLink": {
            '/': '#/',
        },
        # Sidebar Configuration
        "auto2top": True,
        "loadSidebar": True,
        "mergeSidebar": True,
        # loadSidebar: './_sidebar.md',
        "loadNavbar": True,
        "maxLevel": 3,
        # Set subMaxLevel to 0 to remove automatic display of page table of contents (TOC) in Sidebar
        "subMaxLevel": 2,
        "sidebarDisplayLevel": 1,

        # Search Plugin Configuration
        "search": {
            "placeholder": 'Type to search',
            "noData": 'No matches found.',
            # Headline depth, 1 - 6
            "depth": 2,
        }
    }

    # Docs(ARGS)
    window.config_doc(ARGS)


def main():
    Head()
    initial()


if __name__ == '__main__':
    main()
