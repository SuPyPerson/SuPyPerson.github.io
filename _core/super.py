# from browser import bind, document, websocket
# from browser.widgets.dialog import InfoDialog
# from .ScriptWidget import ScriptWidget
import json
from collections import namedtuple

Op = namedtuple('Op', "i e d")(*"i e d".split())

'''
class ScriptWidget:

    def __init__(self, browser, script_named=None, main_div_id='', **params):
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
        document, window = browser.document, browser.window
        self.browser = browser
        self.code_text = ""
        m = main_div_id
        # m = main_div_id = f"_{main_div_id}"
        self.script_name = script_named
        self.script_div_id = "script-%s" % main_div_id
        self.name_to_run = params.get("name", None)
        self.console_pre_id = "result_pre-%s" % main_div_id
        self.script_path = "_core/"
        self.main_div_id = main_div_id
        # ScriptVito(did=mid, **params)
        # self.code_text = COD[mid]

        """
        if "alignment" in params and params["alignment"] == 'top-bottom':
            document[main_div_id].innerHTML = widget_code_tb % (m, m, m, m, m, m, m, m)
        else:
            document[main_div_id].innerHTML = widget_code_lr % (m, m, m, m, m, m, m, m)
            if "editor_width" in params:
                document[self.script_div_id].style.width = params["editor_width"]

        document["run-%s" % main_div_id].bind("click", self.run_script)
        document["clear-%s" % main_div_id].bind("click", self.clear_console)
        document["reset-%s" % main_div_id].bind("click", self.get_script)
        """
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
        # self.get_script(COD[main_div_id[1:]])
        # self.ws = self.browser.websocket.WebSocket("http://localhost:8585/ws")

        self.sd = ShareDome(self.editor, ws=None).cria()

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
        self.get_script()

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

            def share(self, ev):
                self.sharing = not self.sharing
                wdg.sd.share(self.sharing)
                self.button.text = self.share_text[self.sharing]
                print("share_script", self.sharing)

            def vai(self):
                return self.button

        h = self.browser.html
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

    def write(self, stn):
        document, timer, python_runner = self.browser.document, self.browser.window, self.browser.python_runner

        def set_svg():
            _ = document[self.console_pre_id] <= stn

        timer.set_timeout(set_svg, 10)

    def clear_console(self, _):
        document, timer, python_runner = self.browser.document, self.browser.window, self.browser.python_runner
        document[self.console_pre_id].innerHTML = ""

    def save_script(self, _):
        pass

    def run_script(self, _):
        document, timer, python_runner = self.browser.document, self.browser.window, self.browser.python_runner
        editor = self.editor  # window.ace.edit(self.script_div_id)
        document[self.console_pre_id].style.color = "dimgrey"
        # sys.stdout = self
        # sys.stderr = ScriptStderr(self.console_pre_id)
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
            # "enableSnippets": True,
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
        self._open()

    def share(self, go=True):
        self.dome = self if go else self.none

    def _open(self):
        websocket = SuperGirls.BR.websocket
        self.open = False
        if not websocket.supported:
            SuperGirls.BR.InfoDialog("websocket", "WebSocket is not supported by your browser")
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

    def on_open(self, e):
        print("on open", e)
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
        print("websocket", f"Message received : {data}")
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
        print("websocket", f"Submitted {len(op)} operations: {json.dumps(op)}")
        self.op = []
        self.ws.send(str(json.dumps(op)))
        # ws.send("ola")

'''


class SuperGirls:
    BR = None

    def __init__(self, browser):
        self.browser = browser
        SuperGirls.BR = browser

    def cria(self):
        # h = self.browser.html
        # div = h.DIV()
        print('Criando super', self.browser.i_d)
        # ScriptWidget(browser=self.browser, script_named="Sup.y.Girls", main_div_id=self.browser.i_d)


def girls(browser):
    sg = SuperGirls(browser)
    return sg.cria()
