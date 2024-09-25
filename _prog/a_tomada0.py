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
    "script_name": "to0", "script_div_id": "to0",
    "height": 200, "title": "Mais Cenas", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
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
    "script_name": "to1", "script_div_id": "to1",
    "height": 200, "title": "Criando Salas", "show_scenario": False, "console_height": 45
}  # _SEC_
from vitollino import Cena, Texto, Jogo, Elemento, INVENTARIO as INV
from cenario import Planilha, Paisagem, Paisagens
from random import shuffle
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
ESCONDIDO = -4000


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
        pass # troque aqui para fazer um baú aparecer

    def acha_garrafa(self, *_):
        self.carta.x = 100 # tras a carta para a cena
        self.garrafa.vai = self.nada_faz

    def nada_faz(self, *_):
        pass

    def aparece_kayke(self, *_):
        # escreva aqui algo semelhante a acha_garrafa
        self.kayke.x = 100
        pass

    def precisa_chave(self):
        pass # faça a chave aparecer

    def tem_chave(self):
        pass # agora faz alguma coisa quando clica no baú

UmaGarrafa()
_SET3_ = {
    "script_name": "jo3", "script_div_id": "jo3",
    "height": 200, "title": "Povoando o Jardim", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
from vitollino import Sala, Elemento, Texto, Jogo
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
cenas = "japones relogio mirante tomjobim".split()
jardim = Sala(*[f"/_ativo/jardim/{cena}.jpg" for cena in cenas])
cena = jardim.sul.vai()
pessoa = "/_ativo/jardim/{}.png"  # este {} vai ser substituído pelo format
personagens = "narciso", "ossanha", "tetis"
narciso, ossanha, tetis = [pessoa.format(personagem) for personagem in personagens]
tetis = Elemento(tetis, x=50, y=300, h=200, cena=cena, texto="A Fecundidade")
ossanha = Elemento(ossanha, x=250, y=300, h=200, cena=cena, texto="O Curandeiro")
narciso = Elemento(narciso, x=450, y=300, h=200, cena=cena, texto="O Orgulhoso")
_SET4_ = {
    "script_name": "jo4", "script_div_id": "jo4",
    "height": 250, "title": "Conversas no Jardim", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
from vitollino import Sala, Elemento, Texto, Jogo
from vitollino import Roteiro, Ator, Fala, A

Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
cenas = "japones relogio mirante tomjobim".split()
jardim = Sala(*[f"/_ativo/jardim/{cena}.jpg" for cena in cenas])
cena = jardim.oeste.vai()
local = "/_ativo/jardim/"
personagens = ("narciso", 450), ("ossanha", 250), ("tetis", 50)
narciso, ossanha, tetis = [Elemento(f"{local}{nome}.png", x=x, y=200, h=300, w=200, cena=cena)
                           for nome, x in personagens]
elenco = (Ator(tetis, "Tetis", 0.4, A.e), Ator(ossanha, "Ossanha", 0.4, A.m),
          Ator(narciso, "Narciso", 0.4, A.d))
falas = [
    Fala(tetis, "Olá, Ossanha você por aqui?", narciso, None),
    Fala(narciso, "Tetis, voce devia falar primeiro comigo", ossanha, None),
    Fala(ossanha, "Rapaz, você se acha o centro do mundo!", narciso, None),
    Fala(narciso, "Do Universo, que eu realmente sou!", tetis, None),
    Fala(tetis, "Eita, não pode ter mais de um deus que dá briga!", tetis, None),
]
Roteiro(cena, falas, elenco)
_SET5_ = {
    "script_name": "jo5", "script_div_id": "jo5",
    "height": 200, "title": "Narciso vira Flor", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
from vitollino import Sala, Elemento, Texto, Jogo
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
as_cenas = "orquidario portal lago palmeiras".split()
jardim = Sala(*[f"/_ativo/jardim/{cena}.jpg" for cena in as_cenas])
cena = jardim.norte.vai()
local = "/_ativo/jardim/"
personagens = ("narciso", 450), ("ossanha", 250), ("tetis", 50)
narciso, ossanha, tetis = [Elemento(f"{local}{nome}.png", x=x, y=300, h=200, cena=cena)
     for nome, x in personagens]
def narciso_vai(*_):
    lago = jardim.sul.vai()
    narciso.entra(lago)
    narciso.vai = lambda _: None
falou = Texto(cena, "Deu para mim, já vou", foi=narciso_vai).vai
narciso.vai = falou