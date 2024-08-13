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
# noinspection PyUnresolvedReferences
from browser import window, ajax, document, html, timer, websocket, run_script as python_runner
from vitollino import Cena, Elemento
import vitollino
import json
from collections import namedtuple

Op = namedtuple('Op', "i e d")(*"i e d".split())

vitollino.STYLE = {'position': "relative", 'width': 800, 'height': '150px', 'minHeight': '150px', 'left': 0, 'top': 0}

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
        self.scenario(did=did, show_scenario=show_scenario, h=h)  # if show_scenario else None

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

        handlers = (self.run_script, self.clear_console, self.get_script,)
        if "alignment" in params and params["alignment"] == 'top-bottom':
            innerHTML = self.widget_code(m, handlers, is_long=True)
            _ = document[main_div_id] <= innerHTML
        else:
            innerHTML = self.widget_code(m, handlers)
            _ = document[main_div_id] <= innerHTML
            if "editor_width" in params:
                document[self.script_div_id].style.width = params["editor_width"]

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
        self.sd = ShareDome(editor=self.editor, ws=None).cria()

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

    def widget_code(self, name, actions, is_long=False):
        """
          <div class="script-title" id="title-%s"></div>
          <div class="script-container" id="script-container-%s">
            <div id="script-%s" class="script-editor-long"></div>
            <div id="result-%s" class="script-result-long"><pre id="result_pre-%s"></pre></div>
          </div>
          <button class="script-button" id="run-%s" type="button">Executar</button>
          <button class="script-button" id="clear-%s" type="button">Limpar Console</button>
          <button class="script-button" id="reset-%s" type="button">Reiniciar</button>
        """
        wdg = self

        class Share:
            def __init__(self):
                self.share_text = "👁 Compartilhar,🕵️‍♀️ Parar".split(",")
                self.sharing = False
                self.button = h.BUTTON("👁 Compartilhar", Class="script-button", Id=f"share-{name}")
                self.button.bind("click", self.share)

            def share(self, _):
                self.sharing = not self.sharing
                wdg.sd.share(self.sharing)
                self.button.text = self.share_text[self.sharing]
                # print("share_script", self.sharing)

            def vai(self):
                return self.button

        h = html
        editor, result = ("script-editor-long", "script-result-long") if is_long else ("script-editor", "script-result")
        buttons = [h.BUTTON("︎▶ Executar", Class="script-button", Id=f"run-{name}"),
                   h.BUTTON("⭕ Limpar Console", Class="script-button", Id=f"clear-{name}"),
                   h.BUTTON("🔁 Reiniciar", Class="script-button", Id=f"reset-{name}"),
                   Share().vai(), ]
        [button.bind("click", action) for button, action in zip(buttons, actions)]

        widget = [
            h.DIV(Class="script-title", Id=f"title-{name}"),
            h.DIV([
                h.DIV(Class=editor, Id=f"script-{name}"),
                h.DIV(h.PRE(id=f"result_pre-{name}"), Class=result, Id=f"result-{name}"),
            ], Class="script-container", Id=f"script-container-{name}"),
        ]
        widget.extend(buttons)
        return widget

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


class ShareDome:
    @staticmethod
    def nop(*_):
        return lambda *_: None

    def __init__(self, editor, ws):
        class ShareNone:
            def __init__(self):
                self.change, self.send, self.do_message = ShareDome.nop, ShareDome.nop, ShareDome.nop
        self.editor = editor
        self.ws = ws
        self.ops = {}
        self.index = 0
        self.open = False
        self.op = []
        self.send = self.do_submit
        self.change = self.do_change
        self.dome = self
        self.none = ShareNone()
        self.share(False)
        # self._open()

    def share(self, go=True):
        self.dome = self if go else self.none
        self._open() if go else None

    def _open(self):
        self.open = False
        if not websocket.supported:
            # SuperGirls.BR.InfoDialog("websocket", "WebSocket is not supported by your browser")
            return
        # open a web socket
        self.ws = ws = websocket.WebSocket("http://localhost:8585/ws")
        # bind functions to web socket events
        ws.bind('open', self.on_open)
        ws.bind('message', self.on_message)
        ws.bind('close', self.on_close)

    def cria(self):
        ed = self.editor
        ed.bind('change', self.on_change)
        self.index = 0

        def ind(d):
            self.index = int(d)

        def edt(d):
            pos = ed.session.doc.indexToPosition(self.index)
            ed.session.insert(pos, d)

        def dlt(d):
            delCt = d
            stPos = ed.session.doc.indexToPosition(self.index)
            edPos = ed.session.doc.indexToPosition(self.index + delCt)
            rangi = {'start': stPos, 'end': edPos}
            ed.session.remove(rangi)

        nv, ops = Op._fields, (ind, edt, dlt)

        self.ops = {k: v for k, v in zip(nv, ops)}
        return self

    def on_open(self, _):
        # print("on open", e)
        self.open = True
        self.send = self.do_submit

    def on_close(self, _):
        self.open = False
        self.share(False)
        # self.send = self.nop

    def on_change(self, e):
        self.dome.change(e)

    def do_change(self, e):
        ed = self.editor
        op = self.op
        st_index = ed.session.doc.positionToIndex(e.start)
        op.append({Op.i: st_index})

        if e.action == 'insert':
            op.append({Op.e: e.lines.join(ed.session.doc.getNewLineCharacter())})
        elif e.action == 'remove':
            try:
                del_go = e.lines
                cnl = ed.session.doc.getNewLineCharacter()
                delCt = len(cnl.join(del_go))
                # delCt = e.lines.join(ed.session.doc.getNewLineCharacter()).length
                op.append({Op.d: delCt})
            except AttributeError:
                print("AttributeError", e.lines)

        self.submit(op)

    def on_message(self, evt):
        self.dome.do_message(evt)

    def do_message(self, evt):
        # message received from server
        self.change = self.nop
        data = evt.data
        # print("websocket", f"Message received : {data}")
        op = json.loads(data)
        # print(op, type(op))
        # [print(k, v) for o in op for k, v in o.items()]
        [self.ops[k](v) for o in op for k, v in o.items()]
        # [print("op", o) for o in op]
        # [self.ops[k](v) for o for k,v do.items() in op]
        self.change = self.do_change

    def submit(self, op):
        self._open() if not self.open else None
        self.send(op)

    def do_submit(self, op):
        # self._open(0) if not self.open else None #self.ws
        # print("websocket", f"Submitted {len(op)} operations: {json.dumps(op)}")
        self.op = []
        self.ws.send(str(json.dumps(op)))
        # ws.send("ola")
