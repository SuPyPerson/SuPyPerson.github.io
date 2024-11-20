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
import json
import sys
from pydoc import replace
from urllib.error import HTTPError
from urllib.request import urlopen

# noinspection PyUnresolvedReferences
from browser import window, ajax, document, html, alert, timer, aio, run_script as python_runner
from browser.session_storage import storage
from browser.local_storage import storage as store

from vitollino import Cena, Elemento, Jogo, STYLE
import vitollino
from os import getenv
from client_facade import MF
# {i: "jaie24", o: "sbce", f: "guia", n: "snct", k: "pyjr", c: "snct/guia",
# j: git + "jaie24/jaie24/", p: git + "sbce/sbce", g: git + "jaie24/guia", m: git + "snct/snct",l: git + "pyjr"
SPR = "k"
GUIDES = "nifk"
GUIA = {k: v for k, v in zip("ionkjpml", "ffcqggcf")}
HOST = "localhost:8080"
PLB = "_PYNO_LOCAL_BOARD"
vitollino.STYLE = {'position': "relative", 'width': 800, 'height': '150px', 'minHeight': '150px', 'left': 0, 'top': 0}
COD = {}
HEADER = {}
MAPAS = {}
"""Store the code and header obtained from the script in the Python file"""


def show(did="0"):
    build_(did=did, name="forest_0.py")


def build(name="forest_0.py"):
    ScriptBuilder(script_name=name).get_script(name)


class ScriptVito:
    def __init__(self, did="0", **params):
        self.did = did
        self.scene = None
        self.e = Elemento
        self.vit = ''
        if "# _VIT_" in COD[did]:
            self.vit, COD[did] = COD[did].split("# _VIT_\n")
        # print(params)
        show_scenario = params.get("show_scenario", True)
        h = None if show_scenario else 1
        self.scenario(did=did, show_scenario=show_scenario, h=h)  # if show_scenario else None

    def executar(self):
        # print("executando", curumim, self.curumim, self.scene, self.did, self.mapa, MAPAS[self.did])
        return MAPAS[self.did][1]

    def prepara(self, mapa):
        from kwarwp.kwarapp import main as kwp_main, Indio
        oid = f"_{self.did}_"
        kwarwp = lambda ind: kwp_main(vitollino=Jogo, medidas=STYLE, mapa=mapa, indios=(ind,), tela=document[oid])

        MAPAS[self.did] = (mapa, kwarwp, Indio)

    def scenario(
            self, did="0", show_scenario=True, sky="_media/sky.gif", sun="_media/sun.gif", soil="_media/terra.jpg",
            ground=200, h=None):
        h = f"{h}px" if h is not None else "300px"
        vitollino.STYLE = {'position': "relative", 'width': "100%", 'height': h, 'minHeight': h, 'left': 0, 'top': 0}

        _did = f"_{did}"
        edi = html.DIV(Id=_did)
        vit = html.DIV(Id=_did + "_", style={"min-height": h, "margin-top": "25px"})
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
        exec(self.vit, dict(c__=c, v__=vitollino, kwarwp_prepara=self.prepara))
        # exec(self.vit, dict(c__=c, v__=vitollino, kwarwp_prepara=lambda m: self.prepara(m)))


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

    def warn(self, err):
        document[self.__console_pre_id].style.color = "green"
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

    def __init__(self, script_name=None, code_name=None, main_div_id='', **params):
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
        document[mid].insertAdjacentElement("afterend", html.DIV(Id=m, Class="script-main-div_"))
        self.script_name, self.code_name = script_name, code_name
        self.guide_anchor = f"#{script_name.split('_')[-1]}"
        self.script_div_id = "script-%s" % main_div_id
        self.name_to_run = params.get("name", None)
        self.console_pre_id = "result_pre-%s" % main_div_id
        self.console = ScriptStderr(self.console_pre_id)
        self.script_path = "_core/"
        self.script_title = params.get("title", "main").replace(" ","_")+".py"
        self.main_div_id = main_div_id
        ScriptVito(did=mid, **params)
        self.code_text = COD[mid]
        from editor_widget import main
        import browser
        menu = zip("play paste xmark".split(),
                   (self.run_script, lambda *_: self.paste_script(), self.clear_console))
        panes = {"caderno": self.widget_code(m, is_long=True)}
        panes.update({"guia": self.create_script_tag()}) if SPR in GUIDES else None
        functions = zip("rotate piggy-bank receipt cloud-bolt cloud".split(),
                        (lambda *_: self.reset_script(), lambda *_: self.save_script(),
                         lambda *_: self.load_script(), lambda *_: self.fetch_script(), lambda *_: self.push_script()))
        if "alignment" in params and params["alignment"] == 'left-right':
            main(browser, menu=menu, panes=panes, pane=document[main_div_id], functions=functions)
            if "editor_width" in params:
                document[self.script_div_id].style.width = params["editor_width"]
            # _ = document[main_div_id] <= self.widget_code(m, main())
        else:
            main(browser, menu=menu, panes=panes, pane=document[main_div_id], functions=functions)
            # _ = document[main_div_id] <= self.widget_code(m, is_long=True)
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

    def paste_script(self):
        src = PLB
        editor = self.editor.getValue()
        clip = storage.get(src, editor)
        self.get_script(clip)
        storage[src] = editor
        window.navigator.clipboard.writeText(editor)
        self.console.warn("Código antigo substituído, clique 📋 (colar) para retornar")

        # alert(f"{self.guide_anchor} foi salvo temporariamente")

    def exec_from_load(self, module, stor=store):
        src = PLB+module if stor is store else ""
        if src in stor:
            # exec(stor[src], dict(__use__=self.exec_from_load))
            _code = stor[src]
            return _code
        else:
            # alert(f"{PLB+module} não estava salvo")
            git_name = self.get_git()
            self.console.write(f"Não estava salvo: {git_name}")

        return ""

    def fetch_script(self, getter=None):
        def get_result(result):
            storage[PLB] = self.editor.getValue()
            self.get_script(result)
            self.console.warn("Código antigo substituído, clique 📋 (colar) para retornar")
        git_name = self.get_git()
        try:
            MF().raw_get(git_name, getter if getter is not None else get_result)
        except HTTPError as e:
            self.console.write(f"Não encontrado: {git_name} - {e}, salve na nuvem ☁️ primeiro")

    def get_git(self):
        name = self.script_name.split("#")[-1] if "#" in self.script_name else self.script_name
        name = self.code_name.split("-") if self.code_name else name.split("-")
        print("get git", name)
        return "/".join(name)

    def load_script(self, stor=store):
        # src = PLB+self.guide_anchor if stor is store else ""
        src = PLB+self.main_div_id if stor is store else ""
        if src in stor:
            self.get_script(stor[src])
            storage[PLB] = self.editor.getValue()
            self.console.warn("Código antigo substituído, clique 📋 (colar) para retornar")
        else:
            # alert(f"{self.main_div_id} não estava salvo")
            git_name = self.get_git()
            self.console.write(f"Não estava salvo: {git_name}, Salve localmente 🐖 primeiro")

    def push_script(self, src=None):

        def on_complete(msg):
            tag = json.loads(msg.read())
            tag = f'{tag["content"]["path"]} salvo' if "content" in tag else "falhou ao salvar"
            recover = ", clique 🌩️ (baixar da nuvem) para ler de volta" if "content" in tag else ""
            self.console.warn(f"Código {tag}, no repositório{recover}")

        def getter(result):
            # print("push_script getter", result)
            sha = result["sha"] if "sha" in result else None

            r = MF().save(code=git_name, data=self.editor.getValue(), sha=sha, hook=on_complete)

        git_name = self.get_git()
        # print("save_script", git_name)
        MF().get(git_name, getter)

    def save_script(self, src=None):
        # store[PLB+self.guide_anchor] = self.editor.getValue()
        store[PLB+self.main_div_id] = self.editor.getValue()
        git_name = self.get_git()
        self.console.warn(f"Código {git_name} salvo, clique 🧾 (recibo) para ler de volta")

    def create_script_tag(self, src=None):
        GUIDE = f"{HOST}?rel={GUIA[SPR]}#/"
        src = src or GUIDE
        # src += self.guide_anchor
        anchor = self.guide_anchor.split("#")
        print("create_script_tag", anchor, GUIDE)
        src = f"{src}{anchor[1]}#{anchor[-1]}"
        oid, anchor = "_if_"+"-".join(anchor), anchor[-1]

        _tag = html.IFRAME(src=src, id=f"oi-{oid}", title="Guia do Agente", name=oid, width="100%", height="600")
        return _tag, lambda *_: None

    def widget_code(self, name, actions=None, is_long=False, button=None):
        def paste(*_):
            # async def do_paste():
            async def do_paste(*_):
                print("widget_code before")
                text = await window.navigator.clipboard.readText()
                print("widget_code", text[100:])

                self.get_script(text)

            timer.set_timeout(lambda *_: aio.run(do_paste()), 300)
            return
        h = html
        actions = actions or (self.run_script, paste, self.clear_console, self.get_script,)
        editor, result = ("script-editor-long", "script-result-long") if is_long else ("script-editor", "script-result")
        buttons = [h.BUTTON("︎▶ Executar", Class="script-button", Id=f"run-{name}"),
                   h.BUTTON("➕ Colar", Class="script-button", Id=f"paste-{name}"),
                   h.BUTTON("⭕ Limpar Console", Class="script-button", Id=f"clear-{name}"),
                   h.BUTTON("🔁 Reiniciar", Class="script-button", Id=f"reset-{name}")]
        buttons = button or buttons
        [button.bind("click", action) for button, action in zip(buttons, actions)]

        widget = [
            h.DIV(Class="script-title", Id=f"title-{name}"),
            h.DIV([
                h.DIV(Class=editor, Id=f"script-{name}"),
                h.DIV(h.PRE(id=f"result_pre-{name}"), Class=result, Id=f"result-{name}"),
            ], Class="script-container", Id=f"script-container-{name}"),
        ]
        # widget.extend(buttons)
        return widget, lambda *_: None

    def write(self, strn):
        def set_svg():
            _ = document[self.console_pre_id] <= strn

        timer.set_timeout(set_svg, 10)

    def clear_console(self, *_):
        document[self.console_pre_id].innerHTML = ""

    def run_script(self, *_):
        editor = self.editor  # window.ace.edit(self.script_div_id)
        document[self.console_pre_id].style.color = "dimgrey"
        sys.stdout,  oid = self, self.main_div_id[1:]
        sys.stderr = ScriptStderr(self.console_pre_id)
        _, tarefa, kaiowa = MAPAS[oid] if oid in MAPAS else [None]*3
        if self.name_to_run is None:
            exec(editor.getValue(),
                 dict(a_tarefa=tarefa, Kaiowa=kaiowa, __name__="__main__", __use__=self.exec_from_load))
        else:
            python_runner(editor.getValue(), self.name_to_run)

    def reset_script(self, code=None):
        storage[PLB] = self.editor.getValue()
        self.console.warn("Código antigo substituído, clique 📋 (colar) para retornar")
        self.get_script(code)

    def get_script(self, code=None):
        code = code if code is not None else self.code_text
        self.editor.setValue(code, -1)
        self.editor.setTheme("ace/theme/gruvbox")
        self.editor.getSession().setMode("ace/mode/python")
        self.editor.setOptions({
            "enableBasicAutocompletion": True,
            "enableSnippets": True,
            "enableLiveAutocompletion": True
        })
