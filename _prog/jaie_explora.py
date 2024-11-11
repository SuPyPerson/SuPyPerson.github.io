# Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
# PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
_SET0_ = {
    "script_name": "caderno_explora", "script_div_id": "caderno_ten",
    "height": 200, "title": "Python em 10 Min", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
# procure dicas no Guia
bichos = "escolha um bicho da amazônia: a-tracajá b- elefante c-jacaré"
bicho = input(bichos)
_SET1_ = {
    "script_name": "caderno_explora#a-caatinga", "script_div_id": "caderno_cen",
    "height": 200, "title": "Caminhando nos Biomas", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
# procure dicas no Guia
from vitollino import Cena, Jogo
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
Cena("_cenas/pantanal1.jpg").vai()
_SET2_ = {
    "script_name": "caderno_explora#a-praia", "script_div_id": "caderno_ato",
    "height": 200, "title": "Perigos para os Biomas", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
# procure dicas no Guia
from vitollino import Cena, Jogo, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena = Cena("_cenas/pantanal1.jpg").vai()
Elemento("_ativo/rosalinda.png", x=200, y=300, cena=a_cena)
_SET3_ = {
    "script_name": "caderno_explora#as-paisagens", "script_div_id": "caderno_fal",
    "height": 200, "title": "Cuidando dos Biomas", "show_scenario": False, "console_height": 45
}  # _SEC_
# no vitollino here
# _VIT_
# procure dicas no Guia
from vitollino import Cena, Jogo, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena = Cena("_cenas/pantanal1.jpg").vai()
fala = "A ação humana pode degradar um bioma."
Elemento("_ativo/rosalinda.png", x=200, y=300, texto=fala, cena=a_cena)
_SET4_ = {
    "script_name": "caderno_explora", "script_div_id": "caderno_gua",
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