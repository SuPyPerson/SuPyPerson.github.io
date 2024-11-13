# Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
# PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
_SET0_ = {
    "script_name": "jo0", "script_div_id": "jo0",
    "height": 200, "title": "A Primeira Cena", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
from vitollino import Cena, Texto, Jogo
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
local = "/_ativo/jardim/{}.jpg"  # este {} vai ser substituído pelo format
japones, relogio = local.format("japones"), local.format("relogio")
cena = Cena(japones).vai()
"japones aqui diz que a imagem da cena á aquela da figura japones.jpg"
Texto(cena, "Olá, Vamos construir o Jardim Radical!").vai()
"cena diz o local que vai mostrar o texto que é colocado após a vírgula"
# cena = Cena(relogio).vai()
"Descomente a linha acima, removendo o *# * inicial e execute"
_SET1_ = {
    "script_name": "rec-main.py", "script_div_id": "recicla_main",
    "height": 200, "title": "Mais Cenas", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
"""Módulo rec.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagem
ESCONDE = -4000
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()

class UmaGarrafa:
    def __init__(self):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        p = Paisagem(mapa_praia.j[0]).vai()

        self.garrafa = Elemento(img="/_ativo/agentes/carta_garrafa.png", w=30, h=10,
             x=100, y=300, cena=p, o=0.5, vai=self.acha_garrafa)
        self.garrafa.o = 0.3 #deixa a garrafa transparente
        self.carta = Elemento(img="/_ativo/agentes/carta_velha.jpg", w=250, h=400,
             x=ESCONDE, y=50, cena=p, texto="Mas o que está escrito aqui?", foi=self.aparece_kayke)
        self.kayke = Elemento(img="/_ativo/agentes/kayke.png", w=250, h=400,
             x=ESCONDE, y=50, cena=p, texto="Deixa que eu vou decifrar")

    def acha_garrafa(self, *_):
        self.carta.x = 100 # tras a carta para a cena
        self.garrafa.vai = self.nada_faz

    def nada_faz(self, *_):
        pass

    def aparece_kayke(self, *_):
        # escreva aqui algo semelhante a acha_garrafa
        self.kayke.x = 100
        pass

UmaGarrafa()
_SET2_ = {
    "script_name": "rec-aventura.py", "script_div_id": "recicla_aventura",
    "height": 200, "title": "Criando Salas", "show_scenario": False, "console_height": 45
}  # _SEC_
"""Módulo rec.aventura"""
from vitollino import Cena, Texto, Jogo, Elemento, INVENTARIO as INV
from cenario import Planilha, Paisagem, Paisagens
from random import shuffle, randint
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
ESCONDIDO = -4000
_, __ = -1000, -2000

class UmaGarrafa:
    def __init__(self):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        pg = Paisagens(mapa_praia.j)
        p = pg.norte
        locais = [pg.norte, pg.leste, pg.sul, pg.oeste]
        shuffle(locais)
        alturas = [x for x in range(260, 460, 25)]
        shuffle(alturas)
        distancias = [x for x in range(100, 560, 50)]
        shuffle(distancias)
        p.vai()
        local_carta = locais.pop()

        self.garrafa = Elemento(img="/_ativo/agentes/carta_garrafa.png", w=30, h=10,
             x=100, y=300, cena=p, o=0.5, vai=self.acha_garrafa)
        self.garrafa.o = 0.3 #deixa a garrafa transparente
        self.carta = Elemento(img="/_ativo/agentes/carta_velha.jpg", w=250, h=400,
             x=ESCONDIDO, y=50, cena=p, texto="Mas o que está escrito aqui?", foi=self.aparece_kayke)
        self.kayke = Elemento(img="/_ativo/agentes/kayke.png", w=250, h=400,
             x=ESCONDIDO, y=50, cena=p, texto="Deixa que eu vou decifrar")

        self.bau = Elemento(img="/_ativo/agentes/bau.png", w=50, h=40,
                       x=ESCONDIDO, y=250, cena=locais.pop(),
                       texto="O que tem dentro do baú? Precisa de chave!", foi=self.precisa_chave)
        self.bau.o = 0.4
        self.chave = Elemento(img="/_ativo/agentes/chave.png", w=50, h=40,
                         x=ESCONDIDO, y=250, cena=locais.pop(), texto="Achamos a chave!", foi=self.tem_chave)
        self.chave.o = 0.4

    def tem_bau(self, *_):
        self.kayke.foi = lambda *_: INV.some(self.kayke) # kayke sai de cena
        # troque o _  e invente a explicação que o Kayke viu na carta
        self.kayke.texto = "_"
        # troque _ por randint para o baú aparecer em um lugar qualquer
        self.bau.x = _
        self.bau.y = _

    def acha_garrafa(self, *_):
        self.carta.x = 100 # tras a carta para a cena
        self.garrafa.vai = self.nada_faz # não clica depois da carta

    def nada_faz(self, *_):
        pass

    def aparece_kayke(self, *_):
        # escreva aqui algo semelhante a acha_garrafa troque _ por um valor
        self.kayke.x = _

    def precisa_chave(self):
        self.chave.x = _  # faça a chave aparecer, mude _ por um valor

    def tem_chave(self):
        self.chave.x = 0  # faça a chave sumir
        # troque _ por um texto que descreva o que tem no baú
        self.bau.texto = "_"

UmaGarrafa()
_SET3_ = {
    "script_name": "rec-continua.py", "script_div_id": "recicla_continua",
    "height": 200, "title": "A Aventura Continua", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
"""Módulo rec.continua"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagens
ESCONDE = -4000
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()

class AventuraContinua:
    def __init__(self):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        pg = Paisagens(mapa_praia.j[4:])
        p = pg.norte
        p.vai()

AventuraContinua()
_SET4_ = {
    "script_name": "rec-termina.py", "script_div_id": "recicla_termina",
    "height": 250, "title": "A Aventura Termina", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
"""Módulo rec.termina"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagens
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()

class AventuraTermina:
    def __init__(self):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        pg = Paisagens(mapa_praia.j[4:])
        p = pg.norte
        p.vai()

AventuraTermina()
