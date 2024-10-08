from time import sleep
from unittest import TestCase
from unittest.mock import patch
TXT = """
_SET0_ = {
    "script_name": "jo0", "script_div_id": "jo0",
    "height": 200, "title": "A Primeira Cena", "show_scenario": False, "console_height": 45
}  # _SEC_
a=0
"""
TXT0 = """
_SET0_ = {
    "script_name": "jo0@@", "script_div_id": "ja0@@",
    "height": 200, "title": "A Primeira Cena", "show_scenario": False, "console_height": 45
}  # _SEC_
a=0
"""


class TestScriptBuilder(TestCase):
    @patch("browser.html.BUTTON")
    def setUp(self, but):
        # browser.run_script = lambda *_: None
        self.mod = []

        but.side_effect = lambda x: self.mod.append(x)
        # import browser
        # browser.html.BUTTON = lambda a, *_, **__: self.mod.append(a)
        from ScriptWidget import ScriptBuilder, show
        ScriptBuilder.get_script = lambda *_: None
        self.sb = ScriptBuilder("tester")
        self.sw = show
        self.sb.text = TXT

    def test_set_script_editor(self):
        self.sb.set_script_editor("a=1", "a0", script_name="tester", title="A Primeira Cena")
        self.assertEqual("a=1", self.sb.code)

    def test_get_scripts_callback_mock(self):
        def set_editor(code, *_, **kwargs):
            self.assertEqual("\na=0\n", code)
            self.assertIn("script_name", kwargs)
            self.assertIn("title", kwargs)
            self.assertEqual("A Primeira Cena", kwargs["title"])
        self.sb.set_script_editor = set_editor
        self.sb.get_scripts_callback(self.sb)

    def test_get_scripts_callback(self):
        bl = self.sb.script_bundle
        self.sb.get_scripts_callback(self.sb)
        self.assertIn("jo0", bl)
        self.assertEqual("A Primeira Cena", bl["jo0"]["title"])

    def test_get_script(self):
        self.assertIsNone(self.sb.get_script(""))

    def _do_test_show(self):
        self.assertIsNone(self.sb.get_script(""))

    def test_show(self):
        self.sb.text = TXT0
        self.sb.get_scripts_callback(self.sb)
        self.sw(did="ja0@@")
        from ScriptWidget import HEADER
        sleep(0.150)
        self._do_test_show()
        assert 'ja0@@' in HEADER, HEADER
        # self.assertIs(browser.html.BUTTON, str)
        self.assertEqual(1, len(self.mod))

