# Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
# PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
_SET0_ = {
    "script_name": "caderno_refina", "script_div_id": "refina_rep",
    "height": 200, "title": "Repensando a História", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
# procure dicas no Guia
class Cenario:
    def __init__(self, azimute=0, lote=0):
        praia = "_ativo/agentes/praia.jpeg"
        praia = Planilha(praia, conta_lado=4.3)
        self.cena = Paisagens(praia.j[lote:]).cenas[azimute]

    def vai(self):
        self.cena.vai()
        return self


if __name__ == "__main__":
    Cenario().vai()
_SET1_ = {
    "script_name": "caderno_refina", "script_div_id": "refina_def",
    "height": 200, "title": "Define Conversa", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
from vitollino import Jogo, Elemento, Texto
from cenario import Planilha, Paisagens
from jogos import Sequencia
JOGO = Jogo(style=dict(height="450px", width="600px"), did="_jogo_")
class TomadaLiteratura:
    def __init__(self, jogo, cenario=None):
        self.jogo = jogo
        self.mapa = Elemento("_ativo/agentes/diagrama_sol.png", x=4, y=160, w=290, h=290)
        mapa_praia = Planilha("_ativo/agentes/praia.jpeg", conta_lado=4.3)
        self.n = n = cenario or Paisagens(mapa_praia.j).norte
        fala = "Na garrafa tinha um pergaminho, mas ele está em tiras, tenho que ajeitar!"
        Elemento("_ativo/maria.png", texto=fala, x=500, y=200, cena=n, foi=self.montar)
    def montar(self):
        Sequencia(self.jogo, "_ativo/agentes/exilio.png", self.n, w=250, h=250,
                  x=10, y=10, dw=2, dh=2, dim=(10, 180, 2))
        '''Monta o jogo da Sequência , para ordenar um conjunto de tiras'''
    def vai(self):
        self.n.vai()
        return self
if __name__ == "__main__":
    TomadaLiteratura(JOGO).vai()
_SET2_ = {
    "script_name": "caderno_refina", "script_div_id": "refina_enc",
    "height": 200, "title": "Encapsula Conversa", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
# procure dicas no Guia
from vitollino import Jogo, Elemento
from cenario import Planilha, Paisagens
from jogos import Associa
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
class TomadaCiente:
    def __init__(self, cenario=None):
        mapa_praia = Planilha("_ativo/agentes/praia.jpeg", conta_lado=4.3)
        self.n = n = cenario or Paisagens(mapa_praia.j).norte
        nomes = "Equador,eixo da terra,gnômon,observador,latitude,horizonte"
        self.nomes = {k[0]: k for k in nomes.split(",")}
        self.maria = Elemento("_ativo/maria.png", x=500, y=200, cena=n)
        self.mapa = Elemento("_ativo/agentes/diagrama_sol.png", x=120, y=10, w=400, h=400, cena=n)
    def associa(self):
        n, nomes = self.n, self.nomes
        associa = Associa(n, caixa=300, borda=20, acertos=3)
        '''Monta o jogo da associação, associando os nomes abaixo com as lacunas'''
        associa.nome(nome=nomes["E"], tit=0, x=185, y=225)
        associa.nome(nome=nomes["e"], tit=1, x=331, y=276)
        associa.nome(nome=nomes["g"], tit=2, x=291, y=35)
        # complete o enigma posicionando todos os nomes no diagrama
        return self
    def vai(self):
        self.n.vai()
if __name__ == "__main__":
    TomadaCiente().associa().vai()
_SET3_ = {
    "script_name": "caderno_refina", "script_div_id": "refina_mon",
    "height": 200, "title": "Montagem Geral", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
# atualize as seções anteriores com dicas no Guia
# salve as seções anteriores clicando no porquinho 🐖
from vitollino import Jogo
JOGO = Jogo(style=dict(height="450px", width="600px"), did="_jogo_")
exec(__use__("_refina_rep"))  # importa o módulo Repensando o Storyboard
exec(__use__("_refina_def"))
c = Cenario(2, 4).vai()
TomadaLiteratura(JOGO, c.cena).vai()

