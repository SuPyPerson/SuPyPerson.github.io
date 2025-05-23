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
    "script_name": "caderno_agente", "code_name": "age-main.py", "script_div_id": "agente_main",
    "height": 200, "title": "Mais Cenas", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
"""Módulo age.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagem
from jogos import Sequencia
ESCONDE = -4000
j = Jogo(style=dict(height="500px", width="650px"), did="_jogo_")


class UmaGarrafa:
    def __init__(self):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        self.p = p = Paisagem(mapa_praia.j[0]).vai()

        self.garrafa = Elemento(img="/_ativo/agentes/carta_garrafa.png", w=30, h=10,
                                x=100, y=300, cena=p, o=0.5, vai=self.acha_garrafa)
        self.garrafa.o = 0.3  # deixa a garrafa transparente
        self.carta = Elemento(img="/_ativo/agentes/carta_velha.jpg", w=250, h=400,
                              x=ESCONDE, y=50, cena=p, texto="Mas o que está escrito aqui?",
                              foi=self.aparece_agente)
        self.agente = Elemento(img="/_ativo/maria.png", w=250, h=400,
                               x=ESCONDE, y=50, cena=p, texto="Deixa que eu vou decifrar",
                               foi=self.o_bilhete)
        texto_bilhete = "Tem um bilhete junto da carta, mas ele está em tiras!"
        self.bilhete = Texto(p, texto_bilhete, foi=self.montar)

    def o_bilhete(self, *_):
        self.carta.x = ESCONDE  # esconde a carta
        self.agente.vai = self.bilhete.vai

    def acha_garrafa(self, *_):
        self.carta.x = 100  # tras a carta para a cena
        self.garrafa.vai = self.nada_faz

    def nada_faz(self, *_):
        pass

    def aparece_agente(self, *_):
        # escreva aqui algo semelhante a acha_garrafa
        self.agente.x = 350
        pass

    def montar(self):
        montou = Texto(self.p, "É a Canção do Exílio do Gonçalves Dias! Mas tem algo atrás!",
                       foi=self.o_diagrama)
        img = "_ativo/agentes/exilio.png"
        poema = Sequencia(j, img, self.p, w=250, h=250, x=10, y=10, dw=2, dh=2,
                          venceu=montou, dim=(10, 180, 2))
        '''Monta o jogo da Sequência , para ordenar um conjunto de tiras'''

    def o_diagrama(self):
        dia = "É o diagrama de um relógio de sol! Temos que achar as peças!"
        mapa = Elemento("_ativo/agentes/diagrama_sol.png", texto=dia,
                        x=4, y=160, w=290, h=290, cena=self.p)
        self.agente.vai = self.nada_faz


UmaGarrafa()
_SET2_ = {
    "script_name": "caderno_agente", "code_name": "age-aventura.py", "script_div_id": "agente_aventura",
    "height": 200, "title": "Criando Salas", "show_scenario": False, "console_height": 45
}  # _SEC_
"""Módulo age.aventura"""
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
        self.kayke.foi = lambda *_: INV.some(self.kayke)  # kayke sai de cena
        # troque o _  e invente a explicação que o Kayke viu na carta
        self.kayke.texto = "_"
        # troque _ por randint para o baú aparecer em um lugar qualquer
        self.bau.x = _
        self.bau.y = _

    def acha_garrafa(self, *_):
        self.carta.x = 100  # tras a carta para a cena
        self.garrafa.vai = self.nada_faz  # não clica depois da carta

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
    "script_name": "caderno_agente", "code_name": "age-continua.py", "script_div_id": "agente_continua",
    "height": 200, "title": "A Aventura Continua", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
"""Módulo age.continua"""
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
    "script_name": "caderno_agente", "code_name": "age-partes.py", "script_div_id": "agente_partes",
    "height": 250, "title": "A Aventura Termina", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
"""Módulo age.partes"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagens
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()

class AventuraPartes:
    def __init__(self):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        pg = Paisagens(mapa_praia.j[4:])
        p = pg.norte
        p.vai()

AventuraPartes()
_SET5_ = {
    "script_name": "caderno_agente#aprende.py", "code_name": "age-aprende.py", "script_div_id": "agente_aprende",
    "height": 250, "title": "A Aventura Termina", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
"""Módulo age.aprende"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagens
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()

class AventuraAprende:
    def __init__(self):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        pg = Paisagens(mapa_praia.j[4:])
        p = pg.norte
        p.vai()

AventuraAprende()
_SET6_ = {
    "script_name": "caderno_agente", "code_name": "age-termina.py", "script_div_id": "agente_termina",
    "height": 250, "title": "A Aventura Termina", "show_scenario": False, "console_height": 45
}  # _SEC_
# document["_so0_"].remove()
# _VIT_
"""Módulo age.termina"""
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

"""Módulo age.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagens
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()


class Inicia:
    """ Esta é a classe principal que deve ficar na aba que começa coma palavra 'Central'"""
    def __init__(self):
        """Neste exemplo você encontra um mapa jogado na areia da praia"""
        i_praia, i_mapa = "_ativo/agentes/praia.jpeg", "_ativo/agentes/pergaminho.png"
        mapa_praia = Planilha(i_praia, conta_lado=4.3)
        self.p = p = Paisagens(mapa_praia.j)
        p.norte.vai()
        self.mapa = Elemento(i_mapa, x=200, y=350, h=20, cena=p.norte, vai=self.ve_mapa)
        """Quando clica no pergaminho perdido ele chama o self.ve_mapa"""
        self.mapa.o, self.cena = 0.2, p.norte

    def ve_mapa(self, *_):
        """Aqui mostra quatro ícones que quando clica leva para as fases"""
        m = self.mapa
        m.o, m.x, m.y, m.w, m.h = 1.0, 100, 10, 400, 400
        self.icon(150, 50, "mountain-sun", "Aqui manda procurar uma caverna próxima", self.caverna)
        self.icon(350, 50, "suitcase", "Existe um baú perdido na praia", self.praia_piratas)
        self.icon(150, 270, "mound", "Tem um artefato ancestral escondido em um sambaqui", self.sambaqui)
        self.icon(350, 270, "church", "Acho que vamos encontrar algo em um templo")

    def icon(self, x, y, ico, diz="", vai=lambda: None, cena=None):
        """Aqui coloca elementos que são ícones que podem ser buscados em
        https://fontawesome.com/search?o=r&m=free """
        cena = cena or self.cena
        style = "font-size: 4em; color: peru;"
        icon = Elemento("_ativo/kwarwp/vazio.png", texto=diz, x=x, y=y, cena=cena, foi=vai)
        """O desenho do elemento é uma figura vazia"""
        icon.elt.html = f'<i class="fa fa-{ico}" style="{style}"></i>'
        """Esta linha bota um ícone da coleção awesome no elemento"""
        """Você pode usar uma imagem no elemento, não precisa usar um ícone"""

    def caverna(self):
        """No caso da caverna, a fase está montada em uma classe semelhante a esta aqui, a Inicia"""
        from age.continua import Aventura
        Aventura()

    def praia_piratas(self):
        """Aqui o código não está dentro duma classe"""
        import age.continua
        pass

    def sambaqui(self):
        """Aqui o código está dentro duma função fase3"""
        from age.parte import fase3
        fase3()


if __name__ == "__main__":
    Inicia()
