# Exercícios para Pensamento Computacional - Montando jardins
# Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
# PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
_SET0_ = {
    "script_name": "ja0", "script_div_id": "ja0",
    "height": 150, "title": "Caminha na Estrada"
}  # _SEC_
from kwarwp.circus import main
from vitollino import Jogo, STYLE
Jogo.Kaiowa = Indio
Jogo.kwarwp = lambda ind: main(vitollino=Jogo, medidas=STYLE, indios=(ind,), tela=c__.tela)
# _VIT_
from vitollino import Jogo as Povo
class Curumim(Povo.Kaiowa):
    def executa(self):
        self.direita()
        self.anda()
        self.anda()
        self.fala("oi")

Povo.kwarwp(Curumim).executa()
