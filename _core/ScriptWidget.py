"""Accessory classes to integrate widgets with docsify.

Classes neste módulo:
    - :py:class:`ScriptVito` include Vitollino scenes in the programming.
    - :py:func:`show` Called when dojo window is opened.
    - :py:func:`build` Called to collect scripts from side script file.
    - :py:class:`ScripStErr` Error Handler Class.
    - :py:class:`ScriptBuilder` Collect scripts from side script file.
    - :py:class:`ScriptWidget` Display Dojo elements in a window.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
.. codeauthor:: Dominik Gront <dgront@gmail.com>

Changelog
---------
.. versionadded::    24.02c
   |br| Fix Script Header reader (29).

.. versionadded::    24.02
   |br| Classes ScriptVito, ScriptWidget (08).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
import sys
from json import loads

from browser import window, ajax, document, html, timer, run_script as python_runner
from vitollino import Cena, Elemento
import vitollino

vitollino.STYLE = {'position': "relative", 'width': 800, 'height': '150px', 'minHeight': '150px', 'left': 0, 'top': 0}

widget_code_lr = """
  <div class="script-title" id="title-%s"></div>
  <div class="script-container" id="script-container-%s">
    <div id="script-%s" class="script-editor"></div>
    <div id="result-%s" class="script-result"><pre id="result_pre-%s"></pre></div>
  </div>  
  <button class="script-button" id="run-%s" type="button">Executar</button>
  <button class="script-button" id="clear-%s" type="button">Limpar Console</button>
  <button class="script-button" id="reset-%s" type="button">Reiniciar</button>
"""

widget_code_tb = """
  <div class="script-title" id="title-%s"></div>
  <div class="script-container" id="script-container-%s">
    <div id="script-%s" class="script-editor-long"></div>
    <div id="result-%s" class="script-result-long"><pre id="result_pre-%s"></pre></div>
  </div>  
  <button class="script-button" id="run-%s" type="button">Executar</button>
  <button class="script-button" id="clear-%s" type="button">Limpar Console</button>
  <button class="script-button" id="reset-%s" type="button">Reiniciar</button>
"""
COD = {}
HEADER = {}
"""Store the code and header obtained from the script in the Python file"""


def show(did="0"):
    build_(did=did, name="forest_0.py")


def build(name="forest_0.py"):
    ScriptBuilder(script_name=name).get_script(name)


class ScriptVito:
    def __init__(self, did="0", **params):
        self.scene = None
        self.e = Elemento
        self.vit = ''
        if "# _VIT_" in COD[did]:
            self.vit, COD[did] = COD[did].split("# _VIT_\n")
        # print(params)
        show_scenario = params.get("show_scenario", True)
        h = None if show_scenario else 1
        self.scenario(did=did, show_scenario=show_scenario, h=h) #  if show_scenario else None

    def scenario(
            self, did="0", show_scenario=True, sky="_media/sky.gif", sun="_media/sun.gif", soil="_media/terra.jpg",
            ground=200, h=None):
        h = f"{h}px" if h is not None else "300px"
        vitollino.STYLE = {'position': "relative", 'width': "100%", 'height': h, 'minHeight': h, 'left': 0, 'top': 0}

        _did = f"_{did}"
        edi = html.DIV(Id=_did)
        vit = html.DIV(Id=_did + "_", style={"min-height": h})
        _ = document[did].parentNode <= vit
        _ = document[did].parentNode <= edi
        if not show_scenario:
            return
        self.scene = c = Cena(img=sky, tela=vit)
        c.elt.style.width = "100%"
        c.img.style.width = "100%"
        c.vai()
        Elemento(img=sun, cena=c)
        Elemento(img=soil, y=100, w=695, h=ground, cena=c)
        exec(self.vit, dict(c__=c, v__=vitollino))


def build_(did="0", name="forest_0.py"):
    def go():
        _did = f"_{did}"
        # print(did, HEADER[did])
        ScriptWidget(script_named=name, main_div_id=did, **HEADER[did])

    timer.set_timeout(go, 100)


class ScriptStderr:
    def __init__(self, console_pre_id):
        self.__console_pre_id = console_pre_id

    def write(self, err):
        document[self.__console_pre_id].style.color = "red"
        document[self.__console_pre_id].innerHTML = err


class ScriptBuilder:

    def __init__(self, script_name, **params):
        """ Creates a collection of widgets in described DIVs
        @param params :
          - height: integer in pixels
          - editor_width: in the case of side-by-side arrangement of windows *editor_width* property defines
            the percentage of the code editor panel; the remaining width will be used by the console
          - alignment: either 'left-right' (the default) or 'top-bottom'
          - read_only: False (default) or True; if True, user won't be able to edit the script
          - hide_buttons: False (default) or True; if True, user won't be able to run the script
          - console_height: integer in pixels - height of the console panel
          - name: name of the module to run; by default this widget just runs the whole script; use
            the ``name`` keyword to run ``__main__`` section of a Python script
        """
        self.script_name = script_name
        self.code = ""
        self.params = params
        self.name_to_run = params.get("name", None)
        self.script_path = "_core/"
        self.get_script(None)


    def set_script_editor(self, code,
                          script_div_id="", **params):
        self.params.update(params)
        self.code = code
        self.params.pop('script_name') if 'script_name' in params else None
        COD[script_div_id] = code.strip()
        HEADER[script_div_id] = dict(code=code, **params)


    def get_scripts_callback(self, request):
        def do_tup(refx, codex):
            import ast
            # params = loads(refx[4:])
            params = ast.literal_eval(refx[4:])
            div_id = params.pop('script_div_id')
            # print("XXX>", loads(refx[4:]), div_id, "XXX>", codex)
            self.set_script_editor(codex, div_id, **params)

        multi = request.text.split("_SET")[1:]
        #
        # print(multi, "\n", multi[0].split("  # _SEC_\n\n"))
        [do_tup(*reference.split("  # _SEC_")) for reference in multi]

    # noinspection PyArgumentList
    def get_script(self, _):
        req = ajax.ajax()
        req.open('GET', self.script_path + self.script_name, True)
        req.set_header('content-type', "application/x-www-form-urlencoded;charset=UTF-8")
        req.bind('complete', self.get_scripts_callback)
        req.send()


class ScriptWidget:

    def __init__(self, script_named=None, main_div_id='', **params):
        """ Creates a widget in a given DIV
        @param params :
          - height: integer in pixels
          - editor_width: in the case of side-by-side arrangement of windows *editor_width* property defines
            the percentage of the code editor panel; the remaining width will be used by the console
          - alignment: either 'left-right' (the default) or 'top-bottom'
          - read_only: False (default) or True; if True, user won't be able to edit the script
          - hide_buttons: False (default) or True; if True, user won't be able to run the script
          - console_height: integer in pixels - height of the console panel
          - name: name of the module to run; by default this widget just runs the whole script; use
            the ``name`` keyword to run ``__main__`` section of a Python script
        """
        mid = main_div_id
        m = main_div_id = f"_{main_div_id}"
        self.script_name = script_named
        self.script_div_id = "script-%s" % main_div_id
        self.name_to_run = params.get("name", None)
        self.console_pre_id = "result_pre-%s" % main_div_id
        self.script_path = "_core/"
        self.main_div_id = main_div_id
        ScriptVito(did=mid, **params)
        self.code_text = COD[mid]


        if "alignment" in params and params["alignment"] == 'top-bottom':
            document[main_div_id].innerHTML = widget_code_tb % (m, m, m, m, m, m, m, m)
        else:
            document[main_div_id].innerHTML = widget_code_lr % (m, m, m, m, m, m, m, m)
            if "editor_width" in params:
                document[self.script_div_id].style.width = params["editor_width"]

        document["run-%s" % main_div_id].bind("click", self.run_script)
        document["clear-%s" % main_div_id].bind("click", self.clear_console)
        document["reset-%s" % main_div_id].bind("click", self.get_script)

        # Set title (number and name) of the script
        index = params.get("index", None)
        title = params.get("title", None)
        if index:
            title_text = "<b>Exemplo %s</b>" % index
            if title:
                title_text += ": %s" % title
            document["title-%s" % main_div_id].innerHTML = title_text

        # Set the height of the editor's window
        self.editor = window.ace.edit(self.script_div_id)
        self.get_script(COD[main_div_id[1:]])

        if "height" in params:
            h = "%dpx" % (params["height"])
        else:
            h = "200px"
        self.editor.container.style.height = h
        self.editor.setReadOnly(params.get("read_only", False))

        document[self.script_div_id].style.height = h
        if "console_height" in params:
            document[self.console_pre_id].style.height = "%dpx" % (params["console_height"])
        else:
            document[self.console_pre_id].style.height = h

        # --- Hide buttons (or not)
        if params.get("hide_buttons", False):
            del document["run-%s" % main_div_id]
            del document["clear-%s" % main_div_id]
            del document["reset-%s" % main_div_id]

    def write(self, strn):
        def set_svg():
            _ = document[self.console_pre_id] <= strn

        timer.set_timeout(set_svg, 10)

    def clear_console(self, _):
        document[self.console_pre_id].innerHTML = ""

    def run_script(self, _):
        editor = self.editor  # window.ace.edit(self.script_div_id)
        document[self.console_pre_id].style.color = "dimgrey"
        sys.stdout = self
        sys.stderr = ScriptStderr(self.console_pre_id)
        if self.name_to_run is None:
            python_runner(editor.getValue())
        else:
            python_runner(editor.getValue(), self.name_to_run)

    def get_script(self, code=None):
        self.editor.setValue(self.code_text, -1)
        self.editor.setTheme("ace/theme/gruvbox")
        self.editor.getSession().setMode("ace/mode/python")
        self.editor.setOptions({
            "enableBasicAutocompletion": True,
            "enableSnippets": True,
            "enableLiveAutocompletion": True
        })
