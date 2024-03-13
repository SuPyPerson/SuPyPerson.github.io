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
"japones aqui diz que a imagem da cena á aquela da figura mirante.jpg"
Texto(cena, "Olá, Vamos construir o Jardim Radical!").vai()
"cena diz a cena que vai mostrar o texto que é colocado após a vírgula"
# cena = Cena(relogio).vai()
"Descomente a linha acima, removendo o *# * inicial e execute"
_SET1_ = {
    "script_name": "jo1", "script_div_id": "jo1",
    "height": 200, "title": "Mais Cenas", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
from vitollino import Cena, Jogo
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
local = "/_ativo/jardim/{}.jpg"  # este {} vai ser substituído pelo format
japones, relogio = local.format("japones"), local.format("relogio")
mirante, tomjobim = local.format("mirante"), local.format("mirante")
cena_japones = Cena(japones)
cena_relogio = Cena(relogio, esquerda=cena_japones)
cena_mirante = Cena(mirante, direita=cena_japones, esquerda=cena_relogio).vai()
cena_relogio.direita = cena_mirante
cena_japones.esquerda = cena_mirante
cena_japones.direita = cena_relogio
cena_mirante = Cena(mirante)  # edite esta linha para ter vizinhos
"agora tente inserir a *cena_mirante* na ciranda"
_SET2_ = {
    "script_name": "jo2", "script_div_id": "jo2",
    "height": 200, "title": "Criando Salas", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
from vitollino import Sala, Elemento, Texto, Jogo
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
cenas = "japones relogio mirante tomjobim".split()
jardim = Sala(*[f"/_ativo/jardim/{cena}.jpg" for cena in cenas])
cena = jardim.sul.vai()
mais_cenas = "orquidario portal lago palmeiras".split()
mais_jardim = Sala()  # complete aqui vendo o exemplo acima
jardim.norte.meio = mais_jardim.norte
#ligue agora o sul do mais_jardim no sul do jardim
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
    "height": 250, "title": "Povoando o Jardim", "show_scenario": False, "console_height": 45
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