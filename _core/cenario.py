""""Accessory classes to improve Vitollino.

Classes neste módulo:
    - :py:class:`Planilha` Vitollino scenes from a SpriteSheet.
    - :py:class:`ScriptWidget` Display Dojo elements in a window.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
.. codeauthor:: Dominik Gront <dgront@gmail.com>

Changelog
---------
.. versionadded::    24.09
   |br| Classes Planilha, Mapa (09).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from vitollino import Sala, Cena
ROSA = ["n", "l", "s", "o"]


class Planilha:
    def __init__(self, imagem, conta_lado=1.1, locais="", tela=None):
        self.imagem, self.tela, self.locais = imagem, tela, locais
        self.conta_lado, self.lado = [int(n) for n in str(conta_lado).split('.')]
        self._i = None
        self.inicia()

    def inicia(self):
        conta, lado = int(self.conta_lado), self.lado
        w, h = int(conta)*100, int(lado)*100
        bs, bi, br, bp = (
            "background-size background-image background-repeat background-position".split())

        def style(p, _w=w, _h=h):
            x, y = (100/conta)*(p % conta), (100/lado)*(p // conta)
            return {
                bs: f"{_w}% {_h}%", bi: f"url({self.imagem})", br: "no-repeat", bp: f"{x:.2f}% {y:.2f}%"}
        self.locais = self.locais or [f"l{i}" for i in range(self.conta_lado*self.lado)]
        self._i = [dict(_im=self.imagem, style=style(i), nome=p)
                   for i, p in enumerate(self.locais)]
        # self._i = [dict(ele=self.imagem, alt=p) for i, p in enumerate(self.locais)]

    def _img(self, posto=0):
        return self._i[posto]
    
    
class Mapa(Planilha):
    def __init__(self, imagem, conta_lado=1.1, locais="", salas="", tela=None):
        self.salas = self.s = self.n = []
        self.nome_salas = salas
        self.tela = tela
        super().__init__(imagem, conta_lado=conta_lado, locais=locais, tela=tela)

    def inicia(self):
        self.conta_lado *= 4
        super(Mapa, self).inicia()
        self.nome_salas = self.nome_salas or [f"s{i}" for i in range(self.conta_lado*self.lado)]
        _img = self._i * 4
        _im4 = list(zip(*(iter(_img),)*4))
        self._im = _imn = list(zip(self.nome_salas, _im4))
        # _imn = zip(self.nome_salas, _im4)

        def do_cena(_im, **kwargs):
            c = Cena(_im, tela=self.tela)  # , **kwargs)
            c.nome = kwargs.get("nome", "_CENA_")
            return c
        def do_teste(_im, **kwargs):
            return kwargs
        self.salas = [{k: do_cena(**v) for k, v in zip(ROSA, sala)} for sala in _im4]
        self._im = {nome: do_teste(nome, **{k: do_cena(**v) for k, v in zip(list(ROSA), sala)}) for nome, sala in _imn}
        self.n = {nome: Sala(nome=nome, **{k: do_cena(**v) for k, v in zip(list(ROSA), sala)}) for nome, sala in _imn}
        self.s = [self.n[nome] for nome in self.nome_salas]

