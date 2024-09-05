_SET6_ = {
    "script_name": "al6", "script_div_id": "al6",
    "height": 150, "title": "Caminha na Estrada Sinuosa"
}  # _SEC_
from kwarwp.kwarapp import main as kwarwp_main, Indio
from vitollino import Jogo, STYLE
MAPA = """
||||||
p....|
||||.|
|....|
|.||||
|....&
"""
kwarwp_prepara(MAPA)
# Jogo.Kaiowa[_d_] = Indio
# Jogo.kwarwp = lambda ind: kwarwp_main(vitollino=Jogo, medidas=STYLE, mapa=MAPA, indios=(ind,), tela=c__.tela)
# # Jogo.kwarwp(ind=Indio).executa()
# _VIT_
class Curumim(Kaiowa):
    def executa(self):
        self.direita()
        self.anda()
        # while self.olha() == "VAZIO":
        #     _ = 0  # troque isso pelo comando certo

a_tarefa(Curumim) # .executa()
_SET7_ = {
    "script_name": "al7", "script_div_id": "al7",
    "height": 150, "title": "Caminha na Estrada Melhorado"
}  # _SEC_
from kwarwp.kwarapp import main as kwarwp_main, Indio
from vitollino import Jogo, STYLE
MAPA = """
||||||
p....|
||||.|
|....|
|.||||
|....&
"""
Jogo.Kaiowa = Indio
Jogo.kwarwp = lambda ind: kwarwp_main(vitollino=Jogo, medidas=STYLE, mapa=MAPA, indios=(ind,), tela=c__.tela)
# Jogo.kwarwp(ind=Indio).executa()
# _VIT_
from vitollino import Jogo as Povo
class Curumim(Povo.Kaiowa):
    def caminha(self):
        while self.olha() == "VAZIO":
            _ = 0 # troque isso pelo comando certo

    def executa(self):
        self.caminha()
        # troque de direção e continue caminhando

Povo.kwarwp(Curumim).executa()
_SET8_ = {
    "script_name": "al8", "script_div_id": "al8",
    "height": 150, "title": "Caminha na Estrada Inteligente"
}  # _SEC_
from kwarwp.kwarapp import main as kwarwp_main, Indio
from vitollino import Jogo, STYLE
MAPA = """
||||||
p....|
||||.|
|....|
|.||||
|....&
"""
Jogo.Kaiowa = Indio
Jogo.kwarwp = lambda ind: kwarwp_main(vitollino=Jogo, medidas=STYLE, mapa=MAPA, indios=(ind,), tela=c__.tela)
# Jogo.kwarwp(ind=Indio).executa()
# _VIT_
from vitollino import Jogo as Povo
class Curumim(Povo.Kaiowa):
    def caminha(self):
        while self.olha() == "VAZIO":
            _ = 0 # troque isso pelo comando certo
        self.esquerda()
        while self.olha() != "VAZIO":
            _ = 0 # troque isso pelo comando certo

    def executa(self):
        self.caminha()
        # continue caminhando

Povo.kwarwp(Curumim).executa()
_SET9_ = {
    "script_name": "al9", "script_div_id": "al9",
    "height": 150, "title": "Caminha na Estrada Árdua"
}  # _SEC_
from kwarwp.kwarapp import main as kwarwp_main, Indio
from vitollino import Jogo, STYLE
MAPA = """
||.|||||
|&¨p#¨.|
||#||.||
||.||#||
|.¨#.¨||
|||||.||
"""
Jogo.Kaiowa = Indio
Jogo.kwarwp = lambda ind: kwarwp_main(vitollino=Jogo, medidas=STYLE, mapa=MAPA, indios=(ind,), tela=c__.tela)
# Jogo.kwarwp(ind=Indio).executa()
# _VIT_
from vitollino import Jogo as Povo
class Curumim(Povo.Kaiowa):
    def caminha(self):
        while self.olha() == "VAZIO":
            _ = 0 # troque isso pelo comando certo
        self.esquerda()
        while self.olha() != "VAZIO":
            _ = 0 # troque isso pelo comando certo

    def executa(self):
        # self.caminha()
        self.direita()
        self.empurra()
        # continue caminhando

Povo.kwarwp(Curumim).executa()
