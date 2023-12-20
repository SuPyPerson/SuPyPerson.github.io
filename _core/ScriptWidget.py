import sys
from json import loads

from browser import window, ajax, document, timer, run_script as python_runner

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


class ScriptStderr:
    def __init__(self, console_pre_id):
        self.__console_pre_id = console_pre_id

    def write(self, err):
        document[self.__console_pre_id].style.color = "red"
        document[self.__console_pre_id].innerHTML = err


class ScriptBuilder:

    def __init__(self, script_name, **params):
        """ Creates a collecton of widgets in decibed DIVs
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
        self.script_path = "_static/"
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
        editor = window.ace.edit(sw.script_div_id)
        editor.setValue(code, -1)
        editor.setTheme("ace/theme/solarized_light")
        editor.getSession().setMode("ace/mode/python")
        # document["reset-%s" % script_div_id].unbind("click")
        document["reset-%s" % script_div_id].bind("click", lambda *_: editor.setValue(code, -1))

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
        document[self.console_pre_id].style.color = "black"
        sys.stdout = self
        sys.stderr = ScriptStderr(self.console_pre_id)
        if self.name_to_run is None:
            python_runner(editor.getValue())
        else:
            python_runner(editor.getValue(), self.name_to_run)

    def get_script_callback(self, request):
        editor = window.ace.edit(self.script_div_id)
        editor.setValue(request.text, -1)
        editor.setTheme("ace/theme/dracula")
        editor.getSession().setMode("ace/mode/python")

    def get_script(self, _):
        req = ajax.ajax()
        req.open('GET', self.script_path + self.script_name, True)
        req.set_header('content-type', "application/x-www-form-urlencoded;charset=UTF-8")
        req.bind('complete', self.get_script_callback)
        req.send()