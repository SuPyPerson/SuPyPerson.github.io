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


class PaneBuilder:
    def __init__(self, pane_id, first_id, jogo_id="_jogo_"):
        self.h, self.p, self.w = PaneEditor.h, PaneEditor.p, PaneEditor.w
        self.pane_id = pane_id
        self.first_id = first_id
        abas = "-bars -display -clapperboard -person-chalkboard -play -xmark".split()
        actions = ["executa", "limpa", "reinicia", "salva", "pega", "fecha"]
        actions = ["-play", "-shower", "-backward-step", "-download", "-upload", "-circle-stop"]
        users = ["alvo", "bola", "casa", "dado"]
        self.panes = [(self.h.IMG(src=f"{self.p}{img}"), self.w+name) for img, name in enumerate(abas)]
        self.panes = [m(f"{face}", None, image) for image, face in self.panes]
        abas = ["-table-list"]+[(aba, lambda ab=aba, *_: self.abre(ab)) for aba in abas]
        uses = ["-user-secret"]+[(aba, lambda ab=aba, *_: self.user(ab)) for aba in users]
        actions = ["-bullseye"]+[(aba, lambda ab=aba, *_: self.user(ab)) for aba in actions]
        menus = [abas, uses, actions, "-download", "-upload", "-circle-stop"]
        self.pane = PaneEditor(pane_id, self.panes, menus)
        self.pane.show()

    def abre(self, aba):
        pass

    def user(self, member):
        pass


class PaneEditor:
    h = None
    d = None
    p = "https://picsum.photos/600/450?random="
    w = "fa-solid fa"

    def __init__(self, pane=None, panes=None, menus=None):
        self.pane = pane
        self.tabs = self.h.NAV()  # Class="tab_link")
        _ = pane <= self.tabs
        self.panes = [(self.h.IMG(src=f"{self.p}{img}")) for img in range(3)]
        # self.button = self.build_button("Abra o exercício", self.show, pane=self.d["pydiv"], elt=self.h.BUTTON)
        self.panes = panes or [m(f"exercício{face}", None, image) for face, image in enumerate(self.panes)]
        self.panes = self.create_panes()
        menu = [pn.repr() for pn in self.panes]
        menus = zip("-bars -play -xmark".split(), (self.nop(), self.play, self.hide))
        menu += [m(f"{self.w}{face}", action, None) for face, action in menus]
        menu = [menu.pop(-3)] + menu[:-2] + menu[-2:]
        self.menus = ms = self.create_menu(menu, parent=self.tabs)
        self.create_menu(menu[1:], parent=ms[0])

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


CSS = """
 /* Style the tab */
.tab_link {
  overflow: hidden;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
}

/* Style the buttons that are used to open the tab content */
.tab_link button {
  background-color: inherit;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 2px 16px;
  transition: 0.3s;
}

/* Change background color of buttons on hover */
.tab_link button:hover {
  background-color: #ddd; !important;
}

/* Create an active/current tab_link class */
.tab_link button.active {
  background-color: #ccc;!important;
}

/* Style the tab content */
.tab_content {
  display: none;
  padding: 2px 12px;
  border: 1px solid #ccc;
  border-top: none;
} 
html, body{
   padding:0px;
   margin:0px;
   background:#191A1D;
   font-family: 'Karla', sans-serif;
   width:100vw;
}
body * {
   margin:0;
   padding:0;
}

/* HTML Nav Styles */
/* HTML Nav Styles */
/* HTML Nav Styles */
nav menuitem {
   position:relative;
   display:block;
   opacity:0;
   cursor:pointer;
}

nav menuitem > menu {
   position: absolute;
   pointer-events:none;
}
nav > menu { display:flex; }

nav > menu > menuitem { pointer-events: all; opacity:1; }
menu menuitem a { white-space:nowrap; display:block; }
   
menuitem:hover > menu {
   pointer-events:initial;
}
menuitem:hover > menu > menuitem,
menu:hover > menuitem{
   opacity:1;
}
nav > menu > menuitem menuitem menu {
   transform:translateX(100%);
   top:0; right:0;
}
/* User Styles Below Not Required */
/* User Styles Below Not Required */
/* User Styles Below Not Required */

nav_ { 
   margin-top: 40px;
   margin-left: 40px;
}

nav a {
   background:#75F;
   color:#FFF;
   min-width:190px;
   transition: background 0.5s, color 0.5s, transform 0.5s;
   margin:0px 6px 6px 0px;
   padding:0px 40px;
   box-sizing:border-box;
   border-radius:5px;
   box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5);
   position:relative;
   font-size: smaller;
}

nav a:hover:before {
   content: '';
   top:0;left:0;
   position:absolute;
   background:rgba(0, 0, 0, 0.2);
   width:100%;
   height:100%;
}

nav > menu > menuitem > a + menu:after{
   content: '';
   position:absolute;
   border:10px solid transparent;
   border-top: 10px solid white;
   left:12px;
   top: -40px;  
}
nav menuitem > menu > menuitem > a + menu:after{ 
   content: '';
   position:absolute;
   border:10px solid transparent;
   border-left: 10px solid white;
   top: 20px;
   left:-180px;
   transition: opacity 0.6, transform 0s;
}

nav > menu > menuitem > menu > menuitem{
   transition: transform 0.6s, opacity 0.6s;
   transform:translateY(150%);
   opacity:0;
}
nav > menu > menuitem:hover > menu > menuitem,
nav > menu > menuitem.hover > menu > menuitem{
   transform:translateY(0%);
   opacity: 1;
}

menuitem > menu > menuitem > menu > menuitem{
   transition: transform 0.6s, opacity 0.6s;
   transform:translateX(195px) translateY(0%);
   opacity: 0;
} 
menuitem > menu > menuitem:hover > menu > menuitem,  
menuitem > menu > menuitem.hover > menu > menuitem{  
   transform:translateX(0) translateY(0%);
   opacity: 1;
}
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

"""


def main(browser, oid, fid="to0", base=None):
    base = base or "_modal_"
    PaneEditor.h = browser.html
    PaneEditor.d = browser.document
    style = PaneEditor.h.STYLE(CSS)
    style.innerHtml = CSS
    _ = browser.document.head <= style
    # _ = PaneEditor(browser.document[base])
    _ = PaneBuilder(browser.document[base], first_id=fid, jogo_id=oid)

