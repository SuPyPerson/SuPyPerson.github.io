# Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
# PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
_SET4_ = {
    "script_name": "al4", "script_div_id": "al4",
    "height": 150, "title": "Caminha na Estrada"
}  # _SEC_
from kwarwp.kwarapp import main as kwarwp_main, Indio
from vitollino import Jogo, STYLE
MAPA = """
||||||
p....&
||||||
"""
kwarwp_prepara(MAPA)
# _VIT_
class Curumim(Kaiowa):
    def executa(self):
        self.direita()
        self.anda()
        self.anda()
        self.fala("oi")

a_tarefa(Curumim).executa()
_SET5_ = {
    "script_name": "al5", "script_div_id": "al5",
    "height": 150, "title": "Caminha na Estrada com Toras"
}  # _SEC_
MAPA = """
|||||||
p.####&
|||||||
"""
kwarwp_prepara(MAPA)
# _VIT_
class Curumim(Kaiowa):
    def executa(self):
        self.direita()
        self.anda()
        for _ in range(2):
            self.pega()
            self.larga()

a_tarefa(Curumim).executa()
_SET6_ = {
    "script_name": "al6", "script_div_id": "al6",
    "height": 150, "title": "Caminha na Estrada Sinuosa"
}  # _SEC_
MAPA = """
||||||
p....|
||||.|
|....|
|.||||
|....&
"""
kwarwp_prepara(MAPA)
# _VIT_
class Curumim(Kaiowa):
    def executa(self):
        self.direita()
        self.anda()
        # while self.olha() == "VAZIO":
        #     _ = 0  # troque isso pelo comando certo

a_tarefa(Curumim).executa()
_SET7_ = {
    "script_name": "al7", "script_div_id": "al7",
    "height": 150, "title": "Caminha na Estrada Melhorado"
}  # _SEC_
MAPA = """
||||||
p....|
||||.|
|....|
|.||||
|....&
"""
kwarwp_prepara(MAPA)
# _VIT_
class Curumim(Kaiowa):
    def caminha(self):
        self.anda()
        # while self.olha() == "VAZIO": tire o comentário
        #     _ = 0 # e troque isso pelo comando certo

    def executa(self):
        self.caminha()
        # troque de direção e continue caminhando


a_tarefa(Curumim).executa()
_SET8_ = {
    "script_name": "al8", "script_div_id": "al8",
    "height": 150, "title": "Caminha na Estrada Inteligente"
}  # _SEC_
MAPA = """
||||||
p....|
||||.|
|....|
|.||||
|....&
"""
kwarwp_prepara(MAPA)
# _VIT_
class Curumim(Kaiowa):
    def caminha(self):
        # while self.olha() == "VAZIO":
        #     _ = 0 # troque isso pelo comando certo
        self.esquerda()
        # while self.olha() != "VAZIO":
        #     _ = 0 # troque isso pelo comando certo

    def executa(self):
        self.caminha()
        # continue caminhando

a_tarefa(Curumim).executa()
_SET9_ = {
    "script_name": "al9", "script_div_id": "al9",
    "height": 150, "title": "Caminha na Estrada Árdua"
}  # _SEC_
MAPA = """
||.|||||
|&¨p#¨.|
||#||.||
||.||#||
|.¨#.¨||
|||||.||
"""
kwarwp_prepara(MAPA)
# _VIT_
class Curumim(Kaiowa):
    def caminha(self):
        # while self.olha() == "VAZIO":
        #     _ = 0 # troque isso pelo comando certo
        self.esquerda()
        # while self.olha() != "VAZIO":
        #     _ = 0 # troque isso pelo comando certo

    def executa(self):
        # self.caminha()
        self.direita()
        self.empurra()
        # continue caminhando

a_tarefa(Curumim).executa()
