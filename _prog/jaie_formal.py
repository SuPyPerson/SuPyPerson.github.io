# Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
# PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
_SET0_ = {
    "script_name": "caderno_formaliza", "script_div_id": "formaliza_cen",
    "height": 200, "title": "Cena da Praia", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
from vitollino import Cena, Jogo, Texto, Elemento
from cenario import Planilha, Paisagens, Posiciona
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
pg = Paisagens(mapa_praia.j)
n, l, s, o = pg.cenas  # obtém as quatro cenas das paisagens
n.vai()
e = "_ativo/marcador.png"
a = Posiciona(e, cena=n)
# um marcador 📍 que você pode arrastar
# use ctrl+v para colar o elemento reposicionado aqui
_SET1_ = {
    "script_name": "caderno_formaliza", "script_div_id": "formaliza_age",
    "height": 200, "title": "Agentes e Missões", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
from vitollino import Cena, Jogo, Elemento
from cenario import Planilha, Paisagens, Posiciona
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
pg = Paisagens(mapa_praia.j)
sul = pg.cenas[2]  # obtém as quatro cenas das paisagens
sul.vai()
maria = Elemento("_ativo/maria.png", x=350, y=250, cena=sul)
mapa = Elemento("_ativo/agentes/diagrama_sol.png", x=250, y=150, cena=sul)
_SET2_ = {
    "script_name": "caderno_formaliza", "script_div_id": "formaliza_lit",
    "height": 200, "title": "Missão literária", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
# procure dicas no Guia
from vitollino import Cena, Jogo, Elemento
from cenario import Planilha, Paisagem
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
pg = Paisagem(mapa_praia.j[0])
pg.vai()
fala = "Na garrafa tinha um pergaminho, acho que é poesia!"
autor = "É de Gonçalves Dias!"
Elemento("_ativo/maria.png", texto=fala, x=500, y=250, cena=pg)
img = "_ativo/agentes/exilio.png"
poema = Elemento(img, texto=autor, x=10, y=20, cena=pg)
_SET3_ = {
    "script_name": "caderno_formaliza", "script_div_id": "formaliza_cie",
    "height": 200, "title": "Missão Científica", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
# procure dicas no Guia
from vitollino import Cena, Jogo, Elemento
from cenario import Planilha, Paisagem
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
pg = Paisagem(mapa_praia.j[2])
pg.vai()
coisas = "relogio.png terra_girando.gif fala.png".split()
r, t, f = [f"_ativo/agentes/{im}" for im in coisas]
m = "_ativo/maria.png"
fala = "O relógio de sol funciona com a rotação da terra"
explica = "explique algo aqui"
Elemento(r, cena=pg, x=200, y=200, w=200, h=200, texto=fala)
Elemento(t, cena=pg, x=50, y=50, texto=explica)
_SET4_ = {
    "script_name": "caderno_formaliza", "script_div_id": "formaliza_gua",
    "height": 200, "title": "Guardiões dos Biomas", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
# procure dicas no Guia
from vitollino import Cena, Jogo, Elemento
from vitollino import Roteiro, Ator, Fala, A
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena = Cena("_cenas/caatinga2.jpg").vai()
ros = Elemento("_ativo/rosalinda.png", x=400, y=350, cena=a_cena)
kar = Elemento("_ativo/snct/karaja.png", x=100, y=350, cena=a_cena)
elenco = (Ator(ros, "Rosalinda", 0.4, A.d),
          Ator(kar, "Karajá", 0.4, A.e))
falas = [
    Fala(ros, "Os povos originários são os guardiões da terra", kar, None),
    Fala(kar, "Agradeço por considerar o nosso papel importante", ros, None),
]
Roteiro(a_cena, falas, elenco)