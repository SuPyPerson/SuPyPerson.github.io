""""Accessory classes to improve Vitollino.

Classes neste módulo:
    - :py:class:`Planilha` Vitollino scenes from a SpriteSheet.
    - :py:class:`Paisagem` A single scene from a SpriteSheet.
    - :py:class:`Paisagens` A single room from a SpriteSheet.
    - :py:class:`Labirinto` Five rooms disposed ina cross from a SpriteSheet.
    - :py:class:`Mapa` A cartesian collection of rooms from a SpriteSheet.
    - :py:class:`Posiciona` A movable marker that returns chosen coordinates.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    24.11
   |br| Classe  Mapa redefined (22).

.. versionadded::    24.09
   |br| Classes Planilha, Mapa (09).
   |br| Classes Paisagem, Paisagens, Labirinto, PaisagemNula, Typer (16).

|   **Open Source Notification:** This file is part of open source program **Pynoplia**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from vitollino import NoEv, _PATTERN, JOGO, Elemento
from vitollino import Sala, Cena, NADA, Point

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
            if sala == NADA: continue
            self.centro.cenas[indica].meio = sala.cenas[indica]
            indica_oposto = (indica + 2) % 4
            sala.cenas[indica_oposto].meio = self.centro.cenas[indica_oposto]


class Mapa(Planilha):
    def __init__(self, imagem, conta_lado=1.1, locais=(), salas=(), tela=None):
        self.salas = self.s = self.n = self.img = []
        self.nome_salas, self.nome_locais = salas, locais
        self.tela = tela
        self.sala = self.local = {}
        super().__init__(imagem, conta_lado=conta_lado, locais=locais, tela=tela)

    def inicia(self):
        # self.conta_lado = self.conta_lado // 4 if self.conta_lado >= 1 else 1
        _conta, _lado = int(self.conta_lado), self.lado
        super().inicia()
        conta_sala = _conta // 4
        self.salas = [Paisagens(self.j[k:]) for k in range(0, _conta*_lado, 4)]
        linhas = [self.salas[k: k+conta_sala] for k in range(0, conta_sala*_lado, conta_sala)]
        linhas = [list(zip(lon, lon[1:], lon[2:])) for lon in zip(*linhas)]
        _ = [Labirinto(c=c, n=n, s=s) for lin in linhas for n, c, s in lin]
        # print(linhas, l)


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

        self.cenas = [PaisagemNula("", tela=self.tela) for _ in range(self.conta_lado)]


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


class Posiciona(Elemento):
    def __init__(self, img, **kwargs):
        super().__init__(img, **kwargs)
        self.o = 0.6
        # self.elemento, alvo = alvo, alvo.elt
        # self.alvo, self.cena, self._ponto = alvo, cena, Point(self.elemento.x, self.elemento.y)
        self.co = {k: kwargs[k] for k in ("x", "y") if k in kwargs}
        # self.co = {k: kwargs[k] for k in ("x", "y", "w", "h", "cena") if k in kwargs}
        # self.ELT = "Elemento({img}, {x}, {y}, {w}, {h}, {cena})"
        self.ELT = 'Elemento("{img}", x={x}, y={y})'
        self.copy = f"Elemento({img})"
        self._ponto = Point(self.x, self.y)
        outer = self

        class Noop:
            def __init__(self):
                self.outer = outer

            def change(self, ev):
                pass

            @staticmethod
            def update_style(styler, new_style, delta=None):
                cur_style = dict(outer.style)
                point = Point(outer.x, outer.y)
                delta = delta if delta else Point(outer.w, outer.h)
                # print("delta.x, delta.y", outer.elt.style.left, outer.elt.style.top, delta.x, delta.y)
                cur_style.update(cursor=styler, left=point.x, top=point.y, width=delta.x, height=delta.y, **new_style)
                cur_style["min-height"] = "{}px".format(delta.y)
                return cur_style

            def next(self, ev):
                # ev.target.style = self.update_style("move", _PATTERN.BCROSS)
                # outer.current = outer.move
                outer.current = outer.noop

            def mouse_over(self, ev):
                ev.preventDefault()
                ev.stopPropagation()

                ev.target.style.cursor = "default"

            def mouse_down(self, ev):
                client = Point(ev.clientX, ev.clientY)
                ev.preventDefault()
                ev.stopPropagation()
                outer.ponto = client - self.outer.ponto
                outer.cursor = outer.current
                return False

            def mouse_move(self, ev):
                pass

            def mouse_up(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                outer.cursor = outer.noop
                # st = self.outer.elt.style
                # width_, height_, left_, top_ = st.width, st.minHeight, st.left, st.top
                # self.outer.elt.title = CURSOR_ELEMENT.format(left_, top_, width_, height_)
                x, y = Point(outer.elt.offsetLeft, outer.elt.offsetTop)
                outer.co.update(dict(x=x, y=y))
                outer.copy = outer.ELT.format(img=outer.img, **outer.co)

        class Move(Noop):
            def mouse_move(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                client = Point(ev.clientX, ev.clientY)
                delta = outer.ponto - client
                outer.x, outer.y = outer.elt.offsetLeft - delta.x, outer.elt.offsetTop - delta.y
                outer.ponto = client

            def mouse_over(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                ev.target.style.cursor = "move"

            def next(self, ev):
                # print("next resize")
                # ev.target.style = self.update_style("grab", _PATTERN.BOKEH)
                outer.current = outer.noop
                # outer.current = outer.resize

        class Resize(Noop):
            def mouse_move(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                client = Point(ev.clientX, ev.clientY)
                # client = Point(ev.x, ev.y)
                rect = self.outer.elt.getBoundingClientRect()
                # origin = Point(rect.left, rect.top)
                # origin = origin + Point(outer.w//2, outer.w//2)
                delta = outer.ponto - client
                delta = Point(outer.w//2, outer.w//2) - delta
                outer.w, outer.h = outer.w + delta.x, outer.h-delta.y
                outer.ponto = client

            def mouse_over(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                ev.target.style.cursor = "grab"

            def next(self, ev):
                # print("next noop")
                ev.target.style = self.update_style("default", _PATTERN.STARRY)
                outer.current = outer.noop

        def next_state(ev):
            # self.state.append(self.state.pop(0))
            JOGO.window.navigator.clipboard.writeText(outer.copy)

            self.current.next(ev)

        def _mouse_down(ev): return self.cursor.mouse_down(ev)

        def _mouse_up(ev): return self.cursor.mouse_up(ev)

        def _mouse_move(ev): return self.cursor.mouse_move(ev)

        def _mouse_over(ev): return self.cursor.mouse_over(ev)

        def _strip_kind(dm):
            kinds = "px %".split()
            kind = [k for k in kinds if isinstance(dm, str) and (k in dm)]
            # dm = str(dm) if isinstance(dm, int) else dm if isinstance(dm, str) else "0"
            return int(dm.rstrip(kind[0])) if kind else int(dm) if dm else 0

        self.noop, self.move, self.resize = self.state = [Noop(), Move(), Resize()]
        self.cursor = self.noop
        self.current = self.move
        self.elt.onclick = next_state
        self.elt.onmousedown = _mouse_down
        self.elt.onmouseup = _mouse_up
        self.elt.onmousemove = _mouse_move
        self.elt.onmouseover = _mouse_over

    @property
    def ponto(self):
        return self._ponto

    @ponto.setter
    def ponto(self, ponto):
        self._ponto = ponto
