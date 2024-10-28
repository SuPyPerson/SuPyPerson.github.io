""""Widget Editor with multiple panels.

Classes neste módulo:
    - :py:class:`PaneEditor` Tabbed Pane.
    - :py:class:`Pane` A single pane with its tab.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    24.09
   |br| Classes PaneEditor, Pane (28).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from collections import namedtuple
m = namedtuple("m", "n a i", defaults=(None, lambda *_: None, None))


class PaneEditor:
    h = None
    d = None
    p = "https://picsum.photos/600/450?random="
    w = "fa-solid fa-"

    def __init__(self, menu=None, panes=None, pane=None, functions=()):
        self.pane = pane
        self.menu = menu
        self.tabs = self.h.NAV()  # Class="tab_link")
        self.panes = panes or {f"exercício{img}": (self.h.IMG(src=f"{self.p}{img}")) for img in range(3)}
        # self.button = self.build_button("Abra o exercício", self.show, pane=self.d["pydiv"], elt=self.h.BUTTON)
        self.panes = [m(face, None, image) for face, image in self.panes.items()]
        self.panes = self.create_panes()
        main_ = [m(f"{self.w}bars", self.nop, None)]
        menus = menu or zip("bars play xmark".split(), (self.nop(), self.play, self.hide))
        menu = main_ + [pn.repr() for pn in self.panes]
        menu += [m(f"{self.w}{face}", action, None) for face, action in menus]
        func = [m(f"{self.w}{face}", action, None) for face, action in functions]
        # print(list(func))
        # menu = [menu.pop(-3)] + menu[:-2] + menu[-2:]
        self.menus = ms = self.create_menu(menu, parent=self.tabs)
        self.create_menu(func, parent=ms[0])
        # self.create_menu(menu[1:], parent=ms[0])
        _ = pane <= self.tabs
        self.panes[0].show()

    def build_button(self, button, action, pane=None, elt=None):
        pane = pane or self.d["pydiv"]
        elt = elt or PaneEditor.h.MENUITEM
        this = elt(button)
        _ = pane <= this
        this.bind("click", lambda event: action())
        return this

    def create_panes(self):
        this = self

        class Pane:
            def __init__(self, h, panne=None, name=None):
                self.name = panne.n
                self.pane = pane_ = h.DIV(panne.i, Class="tab_content")
                _ = _pane <= pane_

            def repr(self):
                return m(self.name, self.show, self.pane)

            def hide(self, *_):
                # self.tab.classList.remove("active")
                self.pane.style.display = "none"

            def show(self, *_):
                this.open_pane()
                # self.tab.classList.add("active")
                self.pane.style.display = "block"

        def create(panne, name=None):
            return Pane(self.h, panne, name)
        _pane = self.pane
        panes = [create(panne) for panne in self.panes]
        return panes

    def create_menu(self, menus, parent=None):
        this = self
        h = self.h

        class Menu:
            def __init__(self, menu):
                name = h.I(Class=menu.n) if "fa-" in menu.n else menu.n
                anchor = h.A(name)
                action = menu.a if menu.a else lambda: None
                anchor.bind("click", lambda event: action())
                self.menu = h.MENUITEM(anchor)
                self.menu.bind("mouseover", lambda event: self.hover())

            def append(self, item):
                _ = item <= self.menu
                return self.menu

            def hover(self):
                self.menu.classList.toggle("hover")

            def no_hover(self):
                self.menu.classList.remove("hover")

        # menus = [Menu(oit).append(parent) for oit in menus]
        menus = [Menu(oit).menu for oit in menus]
        _ = parent <= h.MENU(menus)
        self.d.bind("mouseover", self.reset)
        return menus

    def show(self, *_):
        # print("show", self.pane, self.pane.Id)
        self.pane.style.display = "block"

    def hide(self, *_):
        self.pane.style.display = "none"

    def open_pane(self):
        [pane.hide() for pane in self.panes]

    def limpa(self):
        print("limpa console")

    def reset(self, *_):
        [mn.classList.remove("hover") for mn in self.menus]

    def play(self):
        print("play console")

    def nop(self):
        pass


def main(browser, menu, panes=None, pane=None, functions=()):
    pane = pane or browser.document["_modal_"]
    PaneEditor.h = browser.html
    PaneEditor.d = browser.document
    return PaneEditor(menu, panes=panes, pane=pane, functions=functions)
