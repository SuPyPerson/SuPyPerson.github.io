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
from vitollino import Sala, Cena, SalaCenaNula, Labirinto, NADA

ROSA = ["n", "l", "s", "o"]


class Planilha:
    def __init__(self, imagem, conta_lado=1.1, locais="", tela=None):
        class Lugares:
            pass
        self.imagem, self.tela, self.locais, self.lugares = imagem, tela, locais, None
        self.conta_lado, self.lado = [int(n) for n in str(conta_lado).split('.')]
        self.i, self.j, self.c = None, None, Lugares()
        self.inicia()

    # noinspection PyDefaultArgument
    def inicia(self):
        conta, lado = int(self.conta_lado), self.lado
        w, h = int(conta)*100, int(lado)*100
        bs, bi, br, bp = (
            "background-size background-image background-repeat background-position".split())

        def style(p, _w=w, _h=h):
            conta_ = conta - 1 if conta > 1 else 1
            lado_ = lado - 1 if lado > 1 else 1
            x, y = (100/conta_)*(p % conta), (100/lado_)*(p // conta)
            return {
                bs: f"{_w}% {_h}%", bi: f"url({self.imagem})", br: "no-repeat", bp: f"{x:.2f}% {y:.2f}%"}
        self.locais = self.locais or [f"l{i}" for i in range(self.conta_lado*self.lado)]
        self.i = locais = {nome: style(i) for i, nome in enumerate(self.locais)}
        # [setattr(self.c, k, (lambda x, _v=v: _v)) for k, v in locais.items()]
        [setattr(self.c, k, v) for k, v in locais.items()]
        self.j = [style(i) for i, p in enumerate(self.locais)]
        # self._i = [dict(ele=self.imagem, alt=p) for i, p in enumerate(self.locais)]

    def _img(self, posto=0):
        return self.j[posto]

class Paisagem(Cena):
    def __init__(self, style, tela=None, **kwargs):
        super().__init__("", tela=tela, **kwargs)
        self.elt.html = ""
        self.elt.style = style


class Paisagens(Sala):
    def __init__(self, locais, conta_lado=4, tela=None, n=NADA, l=NADA, s=NADA, o=NADA,
                 nome='', **kwargs):
        super().__init__(n, l, s, o, nome, **kwargs)
        self.cenas = [Paisagem(img, tela=tela) for img in locais[:conta_lado]]
        self.nome = nome
        [setattr(self, rosa, cena) for rosa, cena in zip(ROSA, self.cenas)]
        Sala.c(**kwargs)
        self.p()


class Mapa(Planilha):
    def __init__(self, imagem, conta_lado=1.1, locais="", salas="", tela=None):
        self.salas = self.s = self.n = []
        self.nome_salas = salas
        self.tela = tela
        super().__init__(imagem, conta_lado=conta_lado, locais=locais, tela=tela)
        linha = int(conta_lado)
        salas = [SalaCenaNula]*linha+self.n+[SalaCenaNula]*linha
        matriz_salas = list(zip(*(iter(salas),)*int(conta_lado)))
        matriz_salas = zip(*matriz_salas)
        [[Labirinto(c=c, n=n, s=s) for n, c, s in trio]
         for coluna in matriz_salas for trio in zip(coluna, coluna[1:-1], coluna[2:]+coluna)]

    def inicia(self):
        self.conta_lado *= 4
        super(Mapa, self).inicia()
        self.nome_salas = self.nome_salas or [f"s{i}" for i in range(self.conta_lado*self.lado)]
        _img = self.j * 4
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

