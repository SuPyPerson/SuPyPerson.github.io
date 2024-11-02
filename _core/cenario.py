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
   |br| Classes Paisagem, Paisagens, Labirinto, PaisagemNula, Typer (16).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from vitollino import NoEv
from vitollino import Sala, Cena, NADA

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
        [setattr(self.c, k, v) for k, v in locais.items()]
        self.j = [style(i) for i, p in enumerate(self.locais)]

    def _img(self, posto=0):
        return self.j[posto]


class Paisagem(Cena):
    def __init__(self, style, tela=None, **kwargs):
        super().__init__("", tela=tela, **kwargs)
        self.elt.html = ""
        self.elt.style = style
        self._foi = lambda *_: None

    def rename(self, nome):
        self.nome = nome
        return self

    def vai(self, ev=NoEv()):
        super().vai()
        self._foi(ev)

    @property
    def foi(self):
        return self._foi

    @foi.setter
    def foi(self, foi):
        self._foi = foi


class Paisagens(Sala):
    def __init__(self, locais, conta_lado=4, tela=None, n=NADA, l=NADA, s=NADA, o=NADA,
                 nome='', **kwargs):
        self.locais, self.conta_lado, self.tela, self.kwargs = locais, conta_lado, tela, kwargs
        super().__init__(n, l, s, o, nome, **kwargs)
        self.inicia()

    def rename(self, nome):
        self.nome = nome
        return self

    def inicia(self):
        self.cenas = [Paisagem(img, tela=self.tela) for img in self.locais[:self.conta_lado]]
        self.nome = self.nome
        [setattr(self, rosa, cena) for rosa, cena in zip(ROSA, self.cenas)]
        Sala.c(**self.kwargs)
        self.p()


class Labirinto:
    def __init__(self, c=NADA, n=NADA, l=NADA, s=NADA, o=NADA):
        self.salas = [sala for sala in [c, n, l, s, o]]
        self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas
        self.lb()

    def lb(self):
        for indica, sala in enumerate(self.salas[1:]):
            self.centro.cenas[indica].meio = sala.cenas[indica]# if sala != NADA else None
            indica_oposto = (indica + 2) % 4
            sala.cenas[indica_oposto].meio = self.centro.cenas[indica_oposto]# if sala != NADA else None
            # self.centro.cenas[indica].portal(N=sala.cenas[indica]) if sala != NADA else None
            # indica_oposto = (indica + 2) % 4
            # sala.cenas[indica_oposto].portal(N=self.centro.cenas[indica_oposto]) if sala != NADA else None


class Mapa(Planilha):
    def __init__(self, imagem, conta_lado=1.1, locais="", salas="", tela=None):
        self.salas = self.s = self.n = self.img = []
        self.nome_salas, self.nome_locais = salas, locais
        self.tela = tela
        self.sala = self.local = {}
        super().__init__(imagem, conta_lado=conta_lado, locais=locais, tela=tela)

    def inicia(self):
        def nomeia(oid, ojd, ponto):
            return nome if (nome := ponto.nome) else f"s{ojd}:{oid}"

        def renomeia(oid, ojd, ponto):
            return nome if (nome := ponto.nome) else f"s{ojd}:{oid}"
        self.conta_lado = self.conta_lado // 4 if self.conta_lado >= 1 else 1
        super(Mapa, self).inicia()
        nula, self.salas = PaisagensNula(0), self._check_sala()
        self.imagem = [[nula]*self.conta_lado] + self.salas + [[nula]*self.conta_lado]
        self.img = imagem = list(zip(self.imagem, self.imagem[1:], self.imagem[2:]))
        [Labirinto(c=c, n=n, s=s) for linha in imagem for n, c, s in zip(*linha)]
        self.nome_salas = self.nome_salas or [
            nomeia(i, j, sala) for j, linha in enumerate(self.salas) for i, sala in enumerate(linha)]
        self.nome_locais = self.nome_locais or [f"{s}.{r}" for s in self.nome_salas for r in ROSA]
        # self.sala = {f"l{ln}:{legenda}": sala.rename(f"l{ln}:{legenda}")
        self.sala = {renomeia(ln, legenda, sala): sala.rename(renomeia(ln, legenda, sala))
                     for ln, linha in enumerate(self.salas) for legenda, sala in zip(self.nome_salas, linha)}
        self.local = {f"{sala.nome}.{legenda}": cena.rename(f"{sala.nome}.{legenda}")
                      for linha in self.salas for sala in linha for legenda, cena in zip(ROSA, sala.cenas)}

    def _check_sala(self):
        _map = self

        class NType(Typer):
            def list(self):
                # return NType(self.ref[0])() #_map.imagem
                return self.ref #_map.imagem

            def paisagens(self):
                return self.ref

            def paisagem(self):
                paisagens = [[Paisagens(imagem)] for linha in self.ref for imagem in linha]
                return paisagens
        # return NType(self.imagem[0][0])(self.imagem[0][0])()
        return NType(self.imagem)()


class PaisagensNula(Paisagens):
    def inicia(self):
        class PaisagemNula(Paisagem):
            def portal(self, esquerda=None, direita=None, meio=None, **kwargs):
                return None

            @property
            def meio(self):
                return self._meio

            @meio.setter
            def meio(self, meio):
                pass

        self.cenas = [PaisagemNula("", tela=self.tela) for img in range(self.conta_lado)]


class Typer:

    def __init__(self, ref, type_names="Planilha Paisagem Paisagens Mapa str"):
        self.ref = ref

    def list(self):
        return self.ref

    def str(self):
        return self.ref

    def paisagens(self):
        return self.ref

    def planilha(self):
        return self.ref

    def __def(self):
        return self.ref

    def __call__(self, *args, **kwargs):
        return getattr(self, type(self.ref).__name__.lower())()
