#! /usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of  program Vitollino
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

# noinspection GrazieInspection
"""Jogos para usar com o Vitollino

    Quebra-cabeças para serem usados na construção de outros jogos.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Classes neste módulo:

    :py:class:`Cubos` Quebra Cabeça com cubos que rolam.
    :py:class:`Roteiro` Facilitador de criação de roteiros.
    :py:class:`Swap` Jogo de arrumar as peças de uma imagem.
    :py:class:`Associa` Arrasta o nome para a posição certa.


Changelog
---------
.. versionadded::    24.10
        Adicionou Swap e Associa.

.. versionadded::    22.04
        Criação do módulo de jogos.

.. versionchanged::    22.04.a
        Usa os comandos originais do DOM.

.. versionadded::    22.05
        Criação da classe Roteiro.


.. seealso::

   Documentação geral do SuperPython: `Ajuda do SuperPython`_

.. _`Ajuda do SuperPython`: https://supygirls.readthedocs.io

"""
from vitollino import Cena, Elemento, Texto, JOGO as J
from random import sample
# from browser import alert
from collections import namedtuple

Ator = namedtuple('Elenco', 'ator nome mini alinha')
Fala = namedtuple('Fala', 'ator fala prox age')  # , defaults=(None,)*4)
A = namedtuple('Ali', 'e m d')(-1, 0, 1)

IMGUR = "https://i.imgur.com/{}.jpg"
FUNDO = "qWcEao4"
CENAS = "CRNsfXO swVe1IW jiJY1NY GsdFmpz T6pmXbY dJ4WOIh".split()
OFF = 2000
OFX, OFY = 100, 50


class Roteiro:
    def __init__(self, cena, roteiro, elenco=(), foi=None):
        """Cria um roteiro de falas entre diversos personagens.

        Os parâmetros roteiro e elenco são definidos por tupla nomeadas.

            Ator

                ator:
                    instância de elemento do ator que no diálogo.

                nome:
                    nome que vai aparecer no título do ator.

                mini:
                    fração da altura do ator na miniatura (0.1 a 1.0)

                alinha:

        :param cena: cena onde o diálogo acontece.
        :param roteiro: Um conjunto de falas entre os personagens.
        :param elenco: Caracterização dos personagens.
        :param foi: Número de cubos na horizontal.
        """
        self.dic_ator = {a.ator: a for a in elenco}
        _prox = zip(roteiro, roteiro[1:] + [Fala(None, "", None, None)])
        self.foi = foi if foi else lambda *_: None
        roteiro = [Fala(a, f, g if g else (p.ator if p else None), x) for [a, f, g, x], p in _prox]
        self.elenco, self.roteiro = elenco, roteiro
        self._foi = lambda *_: None
        script = self
        for _ator in elenco:
            _ator.ator.vai = self.nada
            _ator.ator.tit = _ator.nome
            _ator.ator.elt.style.filter = "brightness(30%)"
        protagonista = elenco[0].ator if elenco else roteiro[0].ator
        self.atores = [ator.ator for ator in elenco] if elenco else [ator.ator for ator in roteiro]
        protagonista.vai = self.segue
        protagonista.elt.style.filter = "brightness(100%)"

        class Falar(Texto):
            def __init__(self, ator, fala, prox, act=None, mini=1, **kwarg):
                self.ator, self.fala, self.prox = ator, fala, prox
                self._foi = act or self.nada
                minih = 80 / mini
                self.mini = Elemento(ator.img, cena=cena, w=80, h=80, tipo=f"80px {minih}px",
                                     style=dict(top="20%", margin="-10px 10%"))
                super().__init__(cena, fala, **kwarg)

            def esconde(self, *_):
                self.mini.elt.remove()
                self.ator.elt.style.filter = "brightness(30%)"
                script.testa(self.prox)
                # script.segue()
                # super().esconde()
                self._foi()

            def vai(self, *_):
                super().vai()
                self.ator.elt.style.filter = "brightness(5%)"
                self.ator.vai = self.nada

            @property
            def foi(self):
                return self._foi

            @foi.setter
            def foi(self, value):
                self._foi = value

            def nada(self, *_):
                pass

        self._fala = Falar

    def nada(self, *_):
        pass

    def segue(self, *_):
        ator, fala, prox, action = self.scripter()
        # ator.elt.style.filter = "brightness(30%)"
        fala = self._fala(ator, fala, prox, action, mini=self.dic_ator[ator].mini)  # .vai()
        if prox:
            prox.vai = self.segue
        fala.vai()

    def testa(self, prox, *_):
        if self.roteiro:
            prox.elt.style.filter = "brightness(100%)"
        else:
            for ato in self.atores:
                ato.elt.style.filter = "brightness(100%)"

    def scripter(self, *_):
        return self.roteiro.pop(0)


class Sprite:
    def __init__(self, img="", index=1, dx=1, dy=1, w=900, h=500, o=1, b=0, s=1, **kwargs):
        sty = dict(width=f"{w}px", height=f"{h}px", overflow="hidden", filter=f"blur({b}px)", scale=s, opacity=o)

        class Img:
            STY = "backgroundPositionX backgroundPositionY backgroundSizeX backgroundSizeY".split()

            def __init__(self, image_index, imx=1, imy=1, imw=900, imh=500):
                self.idx, self.idy, self.imw, self.imh = imx, imy, imw, imh
                self.image_index = image_index
                self.slices = dx * dy
                self.dx = dx

                self.style = {k: f"{v}px" for k, v in zip(self.STY, (0, 0, w, h))}
                self.style.update(**sty)
                self.style.update(backgroundImage=f"url({img})")

            def __getitem__(self, ix):
                gx, gy = ix // self.dx, ix % self.dx
                self.style.update(backgroundPositionX=gx, backgroundPositionY=gy)
                return

            def __iter__(self):
                current_slice = 0
                while current_slice < self.slices:
                    yield self.__getitem__(current_slice)
                    current_slice += 1

        from copy import deepcopy
        self.img_ = deepcopy(img) if isinstance(img, dict) else img
        self.index = index
        self._img = img if hasattr(img, "upper") else Img(index)
        style_ = {}

        def to_int(key):
            return [int(cdd[:-1]) for cdd in _style[key].split()]

        img_, _style, _dim = [v for v in img.values()] if isinstance(img, dict) else (img, {}, (0, 0))
        if _style:
            (ox, oy), (dx, dy) = to_int("backgroundPosition"), to_int("background-size")
            style_["backgroundPosition"] = f"{-ox / 100 * w}px {-oy / 100 * h}px"
            style_["background-size"] = f"{dx / 100 * w}px {dy / 100 * h}px"

        style = dict(width=f"{w}px", height=f"{h}px", overflow="hidden", filter=f"blur({b}px)", scale=s)
        style.update(**style_)
        style.update(**{"background-image": f"url({img_})"})
        # noinspection PyCallingNonCallable

    def __getitem__(self, ix):

        return self._img.__getitem__(ix)

    def __iter__(self):
        return self._img.__iter__()


class Cubos:
    CUBOS = None

    def write(self, *_):
        self.foi()

    def __init__(self, cenas, cena=None, tw=None, th=600, nx=4, ny=3, spx=4, spy=3, ofx=OFX, ofy=OFY, foi=None):
        """Jogo que define cubos formando uma cena em cada lado.

        Joga-se clicando em uma das porções cardeais da face do cubo.
        O cubo irá rolar naquela direção.

        :param cenas: Coleção de seis cenas a serem apresentadas.
        :param tw: Tamanho em pixeis de largura da cena.
        :param th: Tamanho em pixeis de altura da cena.
        :param nx: Número de cubos na horizontal.
        :param ny: Número de cubos na vertical.
        :param spx: Colunas do sprite na horizontal.
        :param spy: Linhas do sprite na vertical.
        :param ofx: Deslocamento na horizontal.
        :param ofy: Deslocamento na vertical.
        """

        self.spy, self.spx, self.foi = spy, spx, foi
        _cubos = self

        class Face(Elemento):
            """Representa a face do cubo.

            A face do cubo é sensível ao click em quatro diferentes porções cardeais.
            As porções cardeais são delimitadas pela duas diagonais do cubo.

            """

            def __init__(self, cubo, inx, face, **kwargs):
                """A face pertencente a um cubo do quebra-cabeça.

                :param cubo: O cubo ao qual pertence.
                :param inx: Índice do cubo no quebra-cabeça.
                :param face: Parte do endereço IMGUR da imagem.
                :param kwargs: Parâmetros a serem passados para o elemento 'Vitollino'.
                """
                self.cubo = cubo
                w, h = tw // nx, th // ny
                w = h = min(w, h)
                self.dh = h
                x, y = (inx % nx) * w, (inx // nx) * h
                super().__init__(IMGUR.format(face), x=x + ofx, y=y - OFF + ofy, w=w, h=h,
                                 cena=cena, vai=self.vai,
                                 style={'background-image': "url({})".format(IMGUR.format(face)),
                                        'background-size': f"{tw}px {th}px",
                                        "background-position": f'{-x}px {-y}px'},
                                 **kwargs)
                # self.siz = (tw, th)
                # self.pos = (-x, -y)
                self.yy = y - OFF + ofy
                self.xx = x + OFX
                self.elt.style.width = f"{w}px"
                self.elt.style.height = f"{h}px"
                self.elt.html = ""
                self.quad = 0

            @property
            def xx(self):
                top = self.elt.style.left[:-2]
                return int(top if top else 0)

            @xx.setter
            def xx(self, value):
                self.elt.style.left = "{}px".format(value)

            @property
            def yy(self):
                top = self.elt.style.top[:-2]
                return int(top if top else 0)

            @yy.setter
            def yy(self, value):
                self.elt.style.top = "{}px".format(value)

            def show(self):
                """Mostra esta face do cubo.

                :return: sempre verdadeiro, para indicar que a face está sendo mostrada.
                """
                self.yy += OFF if self.yy < -10 else 0
                return True

            def hide(self):
                """Esconde esta face do cubo.

                :return: sempre falso, para indicar que a face está sendo ocultada.
                """
                self.yy -= OFF if self.yy > 10 else 0
                return False

            def orient(self, ori):
                """ Reorienta a face para refletir as rolagens do cubo.

                :param ori: Quadrante da rotação da face, entre 0 e 3.
                :return: Sempre falso.
                """
                self.elt.style.transform = f"rotate({ori * 90}deg)"
                return False

            def vai(self, evt):
                """Recebe o click na face e calcula qual quadrante cardeal foi clicado.

                Calcula a posição relativa do click na face.
                Determina o click em relação às duas diagonais da face.
                As diagonais são x=-y e x=y+h.

                :param evt: Evento recebido do navegador.
                :return:
                """
                e = evt.target
                dim = e.getBoundingClientRect()
                x = evt.clientX - dim.left
                y = evt.clientY - dim.top
                e, n, h = x - y, x + y, self.dh
                self.quad = 0 if (e > 0) and (n < h) else 1 if (e > 0) and (n > h) else 2 if (e < 0) and (n > h) else 3
                # Cubo.CUBOS.write(f"x: {x} y: {y} qd: {self.quad}")
                self.cubo.go(self.quad)

        class Cubo:
            """Cubo para formar um quebra-cabeças de seis imagens.

            Cada cubo contém um recorte quadrado de cada uma das seis imagens nas suas faces.
            O cubo rola quando se clica na face que esta sendo apresentada (virada para cima).
            Ao rolar, o cubo vai apresentar uma nova face, dada pela direção indicada na rolagem.

            """
            ROLL = [
                [[19, 4, 21, 12], [18, 8, 22, 0], [17, 12, 23, 4], [16, 0, 20, 8], [6, 1, 12, 11], [12, 3, 6, 10]],
                [[5, 22, 13, 16], [9, 23, 1, 19], [13, 20, 5, 18], [1, 21, 9, 17], [2, 13, 8, 7], [0, 7, 10, 13]],
                [[23, 14, 17, 6], [20, 2, 16, 10], [21, 6, 19, 14], [22, 10, 18, 2], [14, 9, 4, 3], [4, 11, 14, 1]],
                [[15, 18, 7, 20], [3, 17, 11, 21], [7, 16, 15, 22], [11, 19, 3, 23], [10, 5, 0, 15], [8, 15, 2, 5]],
            ]
            """Vetor que representa o índice destino da rolagem dado um clique numa face."""

            def __init__(self, inx, faces):
                """Cubo com os recortes das seis imagens nas suas faces.

                :param inx: Índice posicional do cubo no quebra-cabeça, no sentido da leitura.
                :param faces: Lista com as seis imagens que serão apresentadas nas faces do cubo.
                """
                self.faces = [Face(cubo=self, inx=inx, face=face) for face in faces]
                self.face, self.orient = 0, 0

            def roll(self, inx):
                """Rola o dado na direção indicada.

                Caso esta rolagem complete uma das imagens do quebra-cabeça, indica sucesso.

                :param inx: Índice que representa uma combinação da face com a orientação.
                :return: None
                """
                facer, self.orient = inx // 4, inx % 4
                self.face = [face.show() if facer == face_index else face.hide()
                             for face_index, face in enumerate(self.faces)].index(True)
                self.faces[self.face].orient(self.orient)
                Cubo.CUBOS.write("completou com sucesso") if Cubo.CUBOS.complete() else None

            @property
            def inx(self):
                """Índice que representa uma combinação da face com a orientação.

                :return: Índice que representa uma combinação da face com a orientação.
                """
                return self.face * 4 + self.orient

            def go(self, inx):
                go_face_roll = Cubo.ROLL[self.orient][self.face][inx]
                self.roll(go_face_roll)
                _cubos.go()
                # fc1, ot1 = self.face, self.orient
                # Cubo.CUBOS.write(f"inx: {inx} face: {fc0} ori: {ot0} gfr: {go_face_roll} face: {fc1} ori: {ot1} ")

        cena = cena or Cena(IMGUR.format(FUNDO)).vai()
        # tw, th = (tw, tw // nx * ny) if tw else (th // ny * nx, th)
        Cubo.CUBOS = self
        # self.el = Elemento(IMGUR.format(FUNDO), w=300, h=100, cena=cena, style={"color": "white"})
        self.cubos = cubos = [Cubo(inx=inx, faces=cenas) for inx in range(nx * ny)]
        # scrambler = list(range(23)) * (nx*ny//23 + 1)
        scrambler = [ix % 23 for ix, _ in enumerate(cubos)]
        scramble = zip(cubos, sample(scrambler, len(cubos)))
        # [cube.roll(randint(0, 23)) for cube in cubos] * 2
        [cube.roll(face) for cube, face in scramble]
        # [cube.roll(0) for cube in cubos]

    def go(self):
        pass

    def complete(self):
        """Calcula para ver se todos os cubos apresentam a mesma face.

        :return: *True* se todas as faces dos cubos representam a mesma imagem.
        """
        # self.write(set(cubo.inx for cubo in self.cubos))
        return len(set(cubo.inx for cubo in self.cubos)) == 1

from browser.timer import set_timeout
"""Usa o timer do navegador para dar um tempinho inicial"""
SF = {"font-size": "30px", "transition": "left 1s, top 1s"}
"""Dá o tamanho da letra da legenda e faz a legenda se movimentar suavemente quando inicia e acerta"""
VAZIO = "https://i.imgur.com/npb9Oej.png"


class Associa:
    """ Jogo que associa o nome de um objeto com o seu desenho
    """
    CENA = "https://i.imgur.com/AD1wScZ.jpg"
    CELULA = "https://i.imgur.com/tcCj6nw.png"

    class Nome:
        """ Cria uma legenda a ser arrastada para a lacuna correta

        As legendas aparecem inicialmente no local certo e depois de um intervalo vão para o canto esquerdo

        :param nome: o nome que aparece na legenda
        :param  tit: a posição que a legenda assume no lado esquerdo
        :param    x: a posição horizontal da legenda
        :param    y: a posição vertical da legenda
        :param jogo: o jogo que esta legenda aparece
        :param cena: a cena onde o jogo aparece
        :param lacuna: imagem de fundo da lacuna
        :param legenda: imagem de fundo da legenda
        """

        def __init__(self, nome, tit, x, y, cena, jogo, caixa=160, borda=100,
                     lacuna=VAZIO, legenda=VAZIO):
            self.nome, self.tit, self.x, self.y, self.jogo, self.borda = nome, tit, x, y, jogo, borda
            titulo = f"n_{tit}"
            """Este título serve para marcar cada legenda. É usado pelo drop para conferir se é a legenda certa"""
            drop = {titulo: self.acertou}
            """este dicionário determina que somente a legenda que tenha este título vai acionar o método acertou"""
            self.lacuna = J.a(lacuna, x=x, y=y, w=160, h=40, style=SF, cena=cena, drop=drop)
            """Cria um elemento que posiciona a lacuna e aceita um drop do elemento que tem o título correto"""
            self.o_nome = J.a(legenda, tit=titulo, x=x, y=y, w=caixa, h=40, style=SF, cena=cena, drag=True)
            """Cria um elemento que posiciona a legenda e tem o título eceito pela lacuna e pode ser arrastado"""
            self.o_nome.elt.html = f"{nome}"
            """Adiciona o nome no elemento que é a legenda"""
            set_timeout(self.inicia, 1500 + 300 * tit)
            """Inicia um cronômetro (1.5 seg) para o jogador ter um tempinho para ver a solução, cada legenda leva mais tempo"""

        def acertou(self, ev=None, nome=None):
            """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
            self.lacuna.elt.html = ""
            self.o_nome.x = self.x
            self.o_nome.y = self.y
            self.jogo.pontuar()

        def inicia(self, ev=None):
            """Quando inicia coloca interrogações na lacuna e posiciona a legenda à esquerda"""
            self.lacuna.elt.html = "??????????"
            self.o_nome.x = self.borda
            self.o_nome.y = 50 + 40 * self.tit

    def __init__(self, cena, acertou=None, acertos=4, caixa=160, borda=100):
        self.cena, self.caixa, self.borda, self.acertos = cena, caixa, borda, acertos
        self.pontua = 0
        self.acertou = acertou or self.acerta
        '''
        self.mito = self.Nome(nome="mitocôndria", tit=0, x=650, y=150, jogo=self, cena=self.cena)
        self.nucle = self.Nome(nome="núcleo",  tit=1, x=550, y=220, jogo=self, cena=self.cena)
        self.reticulo = self.Nome(nome="retículo", tit=2, x=450, y=100, jogo=self, cena=self.cena)
        self.ribossomo = self.Nome(nome="ribossomo",  tit=3, x=560, y=40, jogo=self, cena=self.cena)
        #self.cena.vai()'''

    def nome(self, nome, tit=0, x=650, y=150):
        return self.Nome(nome=nome, tit=tit, x=x, y=y, caixa=self.caixa, borda=self.borda,
                         jogo=self, cena=self.cena)

    def acerta(self):
        J.n(self.cena, "Você acertou tudo! Parabéns!").vai()

    def pontuar(self):
        self.pontua += 1
        if self.pontua == self.acertos:
            self.acertou()


class Swap:
    """ Jogo que embaralha as partes de um desenho e usa drag and drop para rearrumar.

        As peças aparecem inicialmente embaralhadas e devem ser arrastadas para o local onde deveriam estar

        :param    j: referência ao Jogo do Vitollino.
        :param  img: a imagem que deve ser embaralhada
        :param cena: a cena onde o jogo aparece
        :param    x: a posição horizontal da imagem
        :param    y: a posição vertical da imagem
        :param    w: a largura da imagem
        :param    h: a altura da imagem
        :param   dw: quantidade de colunas que recortam a imagem
        :param   dh: quantidade de linhas que recortam a imagem
    """

    def __init__(self, j, img, cena, w=900, h=400, x=100, y=50, dw=3, dh=3, venceu=None):
        swap = self

        class Peca(j.a):
            """ A Peça representa um recorte da imagem que vai ser embaralhada.
            """

            def __init__(self, local, indice):
                self.local, self.indice = local, indice
                """ local em que a peça foi colocada; local onde a peça deveria estar"""
                pw, ph = w // dw, h // dh
                """largura e altura da peça"""
                lx, ly = x + local % dw * pw, y + local // dw * ph
                """posição horizontal e vertical em pixels onde a peça será desenhada"""
                px, py = indice % dw * pw, indice // dw * ph
                """posição horizontal e vertical em pixels onde o desenho da peça está na imagem"""
                super().__init__(img, x=lx, y=ly, w=pw, h=ph, drag=True, cena=cena)
                """chama o construtor do Elemento Vitollino passandoa as informações necessárias"""
                self.siz = (w, h)
                """redimensiona a figura da imagem para o tamanho fornecido"""
                self.elt.Id = f"_swap_{local}"
                """rotula o elemento da peça com a posição onde foi alocada"""
                self.pos = (-px, -py)
                """reposiciona a figura da imagem para o pedaço que vai aparecer na peça"""
                self.elt.ondrop = lambda ev: self.drop(ev)
                """captura o evento drop da peça para ser tratado pelo método self.drop"""

            def drop(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                src_id = ev.data['text']
                local = int(src_id.split('_')[-1])
                print(f"local -> {local} | indice -> {self.indice}")
                self.dropped(ev, local)

            def dropped(self, ev, local):
                o_outro = swap.pecas[local].pra_la(self, self.x, self.y, local)
                o_local = swap.pecas[local].local
                print(f"indice, o outro -> {self.indice} @ {self.local} <-> {o_outro} @ {o_local}")
                swap.montou()

            def pra_la(self, peca, x, y, local):
                self.local = peca.pra_ca(self.x, self.y, self.local)
                self.x, self.y = x, y
                return self.indice

            def pra_ca(self, x, y, local):
                self.local, local = local, self.local
                self.x, self.y = x, y
                return local

            def certo(self):
                return self.indice == self.local

            def __repr__(self):
                return str(self.indice)

        from random import shuffle
        pecas = list(range(dw * dh))
        shuffle(pecas)
        self.pecas = [Peca(local, indice) for local, indice in enumerate(pecas)]
        self.venceu = venceu or J.n(cena, "Voce venceu!")

    def montou(self):
        resultado = [peca.certo() for peca in self.pecas]
        print(resultado)
        self.venceu.vai() if all(resultado) else None
        return all(resultado)

class Sequencia:
    """Usa um editor de imagem (/) e recorta a imagem em linhas geracionais.
       No game, o jogador terá que clicar nas linhas em ordem certa para montar a imagem corretamente.
    """
    def __init__(self, esta_cena, chama_quando_acerta=lambda: True, dim=(200,20, 200, 50), topo=(50, 100),
                 blocos = ()):
        posiciona_proxima = self.posiciona_proxima
        class LinhaGeracional:
            """Representa cada uma das linhas recortadas da imagem original"""
            def __init__(self, linha, posicao):
                self.x, self.y, self.w, _ = x,y,w,h = dim
                self.posicao = posicao # posição original no topo da página
                self.linha = Elemento(linha, x=x+ posicao*w, y=y, w=w, h=h, cena=esta_cena)
                self.linha.vai = self.clica_e_posiciona_a_linha #quando clica, monta a imagem
            def zera(self):
                self.linha.x = self.x+self.posicao*self.w  # posiciona cada peça com 200 pixels de distância
                self.linha.y = self.y  # posiciona a peça no topo da página
                self.linha.vai = self.clica_e_posiciona_a_linha
            def clica_e_posiciona_a_linha(self, *_):
                x, y = posiciona_proxima(self.posicao)
                if y:  # se o y retornou zero é porque o posiciona próxima detectou montagem errada
                    self.linha.x, self.linha.y = x, y # monta a linha na imagem
                    self.linha.vai = lambda *_:None #desativa o click da linha

        # coloca cada uma das linhas embaralhadas
        self.x, self.y, w_, h_ = dim
        blocos = blocos or [HERDO1, HERDO3, HERDO2, HERDO0]
        self.linhas = [
            LinhaGeracional(linha=uma_linha, posicao=uma_posicao)
            for uma_posicao, uma_linha in enumerate(blocos)]
        self.acertou = chama_quando_acerta
        self.inicia, self.linha_inicial = topo
        self.topo = self.linha_inicial
        self.altura_da_linha = h_  # cada peça do herdograma tem esta altura
        self.posicoes_montadas = []  #lista das linhas já montadas no herdograma
        self.posicoes_corretas = [3, 0, 2, 1]  # lista das linhas montadas corretamente

    def posiciona_proxima(self, posicao):
        """Chamado pelo clique (vai) de cada peça. Atualiza a próxima posição da peça.
           Calcula se montou correto, comparando com a lista de posições corretas.
           Se já montou quatro peças, e não acerto sinaliza com zero, para iniciar o jogo.
        """
        self.linha_inicial += self.altura_da_linha  # incrementa a posição para montar na linha de baixo
        self.posicoes_montadas += [posicao]  # adiciona o índice desta peça na lista de peças montadas
        if self.posicoes_montadas == self.posicoes_corretas:
            self.acertou()  # invoca a ação acertou se montou nas posições corretas
            return self.inicia, self.linha_inicial
        else:
            if len(self.posicoes_montadas) == 4:  # se montou quatro peças incorretas reinicia o game
                [linha.zera() for linha in self.linhas]  # volta as peças para o topo
                self.posicoes_montadas = []  # indica que nenhuma peça foi montada
                self.linha_inicial = self.topo  # inicia a altura de montagem da primeira peça
                return 0, 0  #  retorna uma posição inválida para sinalizar a peça
        return self.inicia, self.linha_inicial

def main():
    cena = J.c(Associa.CENA)
    celula = J.a(Associa.CELULA, x=300, y=50, w=600, h=500, cena=cena)
    # Swap(j=J, img=Associa.CELULA, cena=cena, w=600,h=500,x=300,y=50,dw=3,dh=3)
    associa = Associa(cena, caixa=300, borda=20)
    mito = associa.nome(nome="mitocôndria", tit=0, x=650, y=150)
    nucle = associa.nome(nome="núcleo", tit=1, x=550, y=220)
    reticulo = associa.nome(nome="reticulo", tit=2, x=450, y=100)
    ribossomo = associa.nome(nome="ribossomo", tit=3, x=560, y=40)
    cena.vai()

if __name__ == "__main__":
    from vitollino import STYLE

    STYLE.update(width=850, height="650px")
    # Cubos(CENAS, tw=500, nx=2, ny=2)
HERDO0="https://i.imgur.com/9jsxjLw.png"
HERDO1="https://i.imgur.com/w60bNMG.png"
HERDO2="https://i.imgur.com/RztgWA1.png"
HERDO3="https://i.imgur.com/FZOhJhb.png"
