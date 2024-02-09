import sys
from json import loads

from browser import window, ajax, document, html, timer, run_script as python_runner
from collections import namedtuple
from vitollino import Cena, Elemento
import vitollino

vitollino.STYLE = {'position': "relative", 'width': 800, 'height': '150px', 'minHeight': '150px', 'left': 0, 'top': 0}

# STYLE.update(width="600px", height="200px")
# STYLE["width"] = "100%"
# STYLE["height"] = "200px"
W_text = namedtuple("W_text", "text")

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
WGT = {}
SRC = {}
DIV = []


def show(did="0"):
    # document[did].unbind("click")
    if did not in DIV:
        DIV.append(did)
    print("show", did, DIV)


def build(name="forest_0.py"):
    print("build", name)

    ScriptBuilder(script_name=name).get_script(name)


def build_(did=0, name="forest_0.py"):
    def go():
        # global STYLE
        # STYLE.update(width="600px", height="200px")
        h = "300px"
        vitollino.STYLE = {'position': "relative", 'width': "100%", 'height': h, 'minHeight': h, 'left': 0, 'top': 0}

        _did = f"_{did}"
        edi = html.DIV(Id=_did)
        vit = html.DIV(Id=_did + "_", style={"min-height": h})
        # _ = document[did].src = "_media/sky.gif"

        _ = document[did].parentNode <= vit
        _ = document[did].parentNode <= edi
        c = Cena(img="_media/sky.gif", tela=vit)
        c.elt.style.width = "100%"
        c.img.style.width = "100%"
        '''
        c.elt.style.height = "150px"
        c.elt.style.minHeight = "150px"
        c.img.style.minHeight = "150px"
        c.elt.style.position = "relative"
        c.img.height = 150
        '''
        c.vai()
        e = Elemento(img="_media/sun.gif", cena=c)
        e = Elemento(img="_media/terra.jpg", y=100, w=695, h=200, cena=c)
        e = Elemento(img="_media/animais.png", y=90, x=50, w=200, h=200, cena=c, style={
            "background-size": "200% 300%", "background-position": "100% 50%", 'backdrop-filter': 'hue-rotate(240deg)'})
        e = Elemento(img="_media/capangas.png", y=90, x=250, w=150, h=200, cena=c,
                     style={"background-size": "200% 100%", "background-position": "100% 50%"})
        # print("build", _did, "/_media/sky.gif", c.elt, e.elt)
        if _did not in WGT.keys():
            WGT[_did] = ScriptWidget(script_name=name, main_div_id=_did,
                                     height=150, title="Forest")

    timer.set_timeout(go, 100)


class Widget:

    def __init__(self, did=""):
        div_id = did
        h = "100px"
        # print("Widget", div_id)
        document[div_id].html = ""

        def set_svg():
            # _ = document[self.console_pre_id] <= strn
            editor = window.ace.edit(div_id)
            editor.container.style.height = h
            editor.setReadOnly(False)
            editor.setTheme("ace/theme/gruvbox")
            editor.getSession().setMode("ace/mode/python")
            editor.setValue("print('hello')")
            editor.setOptions({
                "enableBasicAutocompletion": True,
                "enableSnippets": True,
                "enableLiveAutocompletion": True
            })

            document[div_id].style.height = h
            print("done")

        timer.set_timeout(set_svg, 100)

        print("did")
        # from ScriptWidget import ScriptWidget
        # sw2 = ScriptWidget(script_name='forest_0.py', main_div_id=divid)


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
        '''
        # Set title (number and name) of the script
        index = params.get("index", None)
        title = params.get("title", None)
        if "height" in params:
            h = "%dpx" % (params["height"])
        else:
            h = "200px"

        if "console_height" in params:
            console_height = "%dpx" % (params["console_height"])
        else:
            console_height = h

        # --- Hide buttons (or not)
        if params.get("hide_buttons", False):
            hide_buttons = False'''

    def set_script_editor(self, code,
                          script_div_id="", **params):
        self.params.update(params)
        self.code = code
        self.params.pop('script_name') if 'script_name' in params else None
        sw = ScriptWidget(script_name=None, main_div_id=script_div_id, **self.params)
        WGT[script_div_id] = sw
        sw.run_script(0)
        print("get_scripts_callback", script_div_id, params, DIV)
        # editor = window.ace.edit(sw.script_div_id)
        # editor.setValue(code, -1)
        # editor.setTheme("ace/theme/solarized_light")
        # editor.getSession().setMode("ace/mode/python")
        # # document["reset-%s" % script_div_id].unbind("click")
        # document["reset-%s" % script_div_id].bind("click", lambda *_: editor.setValue(code, -1))

    def get_scripts_callback(self, request):
        def do_tup(refx, codex):
            params = loads(refx[4:])
            div_id = params.pop('script_div_id')
            self.set_script_editor(codex, div_id, **params)
            # print("XXX>", loads(refx[4:]))

        multi = request.text.split("_SET")[1:]
        # print(multi, multi[0].split("  # _SEC_\n\n"))
        [do_tup(*reference.split("  # _SEC_")) for reference in multi]
        '''
        editor = window.ace.edit(self.script_div_id)
        editor.setValue(request.text, -1)
        editor.setTheme("ace/theme/solarized_light")
        editor.getSession().setMode("ace/mode/python")'''

    # noinspection PyArgumentList
    def get_script(self, _):
        req = ajax.ajax()
        req.open('GET', self.script_path + self.script_name, True)
        req.set_header('content-type', "application/x-www-form-urlencoded;charset=UTF-8")
        req.bind('complete', self.get_scripts_callback)
        req.send()


class ScriptWidget:

    def __init__(self, script_name=None, main_div_id='', **params):
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
        m = main_div_id
        self.script_name = script_name
        self.script_div_id = "script-%s" % main_div_id
        self.name_to_run = params.get("name", None)
        self.console_pre_id = "result_pre-%s" % main_div_id
        self.script_path = "_core/"
        self.main_div_id = main_div_id
        print("SW", self.script_name, self.script_div_id)
        self.get_script(None) if script_name else None

        if "alignment" in params and params["alignment"] == 'top-bottom':
            document[main_div_id].innerHTML = widget_code_tb % (m, m, m, m, m, m, m, m)
        else:
            document[main_div_id].innerHTML = widget_code_lr % (m, m, m, m, m, m, m, m)
            if "editor_width" in params:
                document[self.script_div_id].style.width = params["editor_width"]

        document["run-%s" % main_div_id].bind("click", self.run_script)
        document["clear-%s" % main_div_id].bind("click", self.clear_console)
        document["reset-%s" % main_div_id].bind("click", self.get_script) if script_name else None

        # Set title (number and name) of the script
        index = params.get("index", None)
        title = params.get("title", None)
        if index:
            title_text = "<b>Exemplo %s</b>" % index
            if title:
                title_text += ": %s" % title
            document["title-%s" % main_div_id].innerHTML = title_text

        # Set height of the editor's window
        self.editor = window.ace.edit(self.script_div_id)
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
        editor = window.ace.edit(self.script_div_id)
        document[self.console_pre_id].style.color = "dimgrey"
        sys.stdout = self
        sys.stderr = ScriptStderr(self.console_pre_id)
        if self.name_to_run is None:
            python_runner(editor.getValue())
        else:
            python_runner(editor.getValue(), self.name_to_run)

    def get_script_callback(self, request):
        SRC[self.script_name] = request.text
        editor = window.ace.edit(self.script_div_id)
        editor.setTheme("ace/theme/gruvbox")
        editor.getSession().setMode("ace/mode/python")
        editor.setOptions({
            "enableBasicAutocompletion": True,
            "enableSnippets": True,
            "enableLiveAutocompletion": True
        })
        editor.setValue(request.text, -1)

    def get_script(self, _):
        if self.script_name in SRC:
            self.get_script_callback(W_text(SRC[self.script_name]))
            return True
        req = ajax.ajax()
        req.open('GET', self.script_path + self.script_name, True)
        req.set_header('content-type', "application/x-www-form-urlencoded;charset=UTF-8")
        req.bind('complete', self.get_script_callback)
        req.send()
