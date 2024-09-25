<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# As Atividades
> E, de repente, o rádio tocou</br>
> Cena de cinema </br>

<img src onerror="__did_got__('../../_prog/o_jogo0.py')"></img>
<div id="_jogo_" style="position:relative; left:50px; min-height: 500px">
Aqui está um elemento identificado como '_jogo_'
</div>

+ Uma Mensagem na Garrafa +  
 
  <img id="jo5" src onerror="__widget__(this.id)"/>
 
  Os Agentes da ESCOLA são chamados para investigar uma mensagem encontrada numa garrafa.
  ```python
  from vitollino import Cena, Texto, Jogo, Elemento
  from cenario import Planilha, Paisagem
  Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
  def aparece_kayke(_):
      Elemento(img="/_ativo/agentes/kayke.png", w=250, h=400,
      x=100, y=50, cena=p, texto="Deixa que eu vou decifrar")
      g.vai = lambda _:None
  def acha_garrafa(_):
      Elemento(img="/_ativo/agentes/carta_velha.jpg", w=250, h=400,
      x=100, y=50, cena=p, texto="Mas o que está escrito aqui?", vai=aparece_kayke)
      g.vai = lambda _:None
  praia = "_ativo/agentes/praia.jpg"
  plan = Planilha(praia, conta_lado=4.3)
  p = Paisagem(plan.j[0]).vai()
  g = Elemento(img="/_ativo/agentes/carta_garrafa.png", w=30, h=10,
  x=100, y=300, cena=p, o=0.5, vai=acha_garrafa)
  g.o = 0.3  
  ```


+ Aventuras na Praia +  
 
  <img id="jo5" src onerror="__widget__(this.id)"/>
 
  A mensagem fala sobre um baú perdido na praia.
  ```python
  from vitollino import Cena, Texto, Jogo, Elemento, INVENTARIO as INV
  from cenario import Planilha, Paisagem, Paisagens
  from random import shuffle
  Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
  def precisa_chave(*_):
    chave.x = distancias.pop()
    chave.y = alturas.pop()
  def sai_kayke(*_):
    agente_kayke.x = -1000
  def tem_bau(*_):
    agente_kayke.foi = lambda *_: INV.bota(agente_kayke)
    agente_kayke._texto = None
    agente_kayke.texto = "Aqui fala de um baú perdido, bora achar!"
    bau.x = distancias.pop()
    bau.y = alturas.pop()
    # agente_kayke.vai = lambda _:None
  def tem_chave(*_):
    INV.bota(chave)
    bau._texto = None
    bau.texto = "Droga! O baú está vazio!"
    # bau.x = 350
  def aparece_kayke(*_):
    carta_velha.x = -1000
    agente_kayke.x = 100
  def acha_garrafa(_):
    carta_velha.x = 150
    g.vai = lambda _:None
  praia = "_ativo/agentes/praia.jpeg"
  plan = Planilha(praia, conta_lado=4.3)
  # pg = Paisagens("", n=plan.j[0],l=plan.j[1], s=plan.j[2],o=plan.j[3]) #.vai()
  pg = Paisagens(plan.j) #.vai()
  p= pg.norte
  locais = [pg.norte, pg.leste, pg.sul, pg.oeste]
  shuffle(locais)
  alturas = [x for x in range(260,460,25)]
  shuffle(alturas)
  distancias = [x for x in range(100,560,50)]
  shuffle(distancias)
  p.vai()
  local_carta = locais.pop()
  g = Elemento(img="/_ativo/agentes/carta_garrafa.png", w=30, h=10,
  x=distancias.pop(), y=alturas.pop(), cena=local_carta, o=0.5, vai=acha_garrafa)
  g.o = 0.3 
  carta_velha = Elemento(img="/_ativo/agentes/carta_velha.jpg", w=250, h=400,
  x=-1000, y=50, cena=local_carta, texto="Mas o que está escrito aqui?", foi=aparece_kayke)
  agente_kayke = Elemento(img="/_ativo/agentes/kayke.png", w=250, h=400,
  x=-1000, y=50, cena=local_carta, texto="Deixa que eu vou decifrar", foi=tem_bau)
  bau = Elemento(img="/_ativo/agentes/bau.png", w=50, h=40,
  x=-1000, y=250, cena=locais.pop(),
  texto="O que tem dentro do baú? Precisa de chave!", foi=precisa_chave)
  bau.o =0.4  
  chave = Elemento(img="/_ativo/agentes/chave.png", w=50, h=40,
  x=-1000, y=250, cena=locais.pop(), texto="Achamos a chave!", foi=tem_chave)
  chave.o =0.4  
  ```

![Em Construção](../_media/em_construcao.png)


#### LABASE
[footer](footer.md ':include')