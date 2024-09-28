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


class PaneEditor:
    h = None

    def __init__(self, pane=None):
        self.pane = pane
        self.panes = [(self.h.IMG(src=f"https://picsum.photos/600/450?random={img}"), f"img{img}") for img in range(3)]
        self.panes = self.create_panes()

    def create_panes(self):
        this = self

        class Pane:
            def __init__(self, h, panne=None, name=None):
                self.pane = pane_ = h.DIV(panne, Class="tab_content")
                self.tab = tab_ = h.BUTTON(name, Class="tab_link")  # _links")
                tab_.bind("click", self.show)
                _ = _tab <= tab_
                _ = _pane <= pane_

            def hide(self, *_):
                self.tab.classList.remove("active")
                self.pane.style.display = "none"

            def show(self, *_):
                this.open_pane()
                self.tab.classList.add("active")
                self.pane.style.display = "block"

        def create(panne, name=None):
            return Pane(self.h, panne, name)
        _pane = self.pane
        _tab = self.h.DIV(Class="tab_link")
        _ = _pane <= _tab
        panes = [create(panne, name) for panne, name in self.panes]
        return panes

    def open_pane(self):
        [pane.hide() for pane in self.panes]


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
  padding: 6px 12px;
  border: 1px solid #ccc;
  border-top: none;
} 
"""


def main(browser):
    PaneEditor.h = browser.html
    style = PaneEditor.h.STYLE(CSS)
    style.innerHtml = CSS
    _ = browser.document.head <= style
    _ = PaneEditor(browser.document["pydiv"])
