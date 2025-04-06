<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# O Agente da SME - Perigo para os Biomas
> E agora para algo totalmente diferente! <br>
> Aprenda Python resolvendo, modificando e criando jogos e desafios. <br>

A ação humana pode ser perigosa para um bioma. Escolha uma opção de jogo

## O desmatamento

```python
from vitollino import Cena, Jogo, Texto
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cena1 = Cena("_cenas/desmatamento4.jpg").vai()
Texto(cena1, "O desmatamento é um perigo para os biomas e a humanidade").vai()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## O garimpo ilegal

```python
from vitollino import Cena, Jogo, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cena1 = Cena("_cenas/grmpilegal.jpg").vai()
fala = "O garimpo ilegal contamina a natureza e os ribeirinhos"
karaja = Elemento("_ativo/snct/karaja.png", x=400, y=150, texto=fala, cena=cena1)
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## O pescador e caçador predatórios

```python
from vitollino import Cena, Jogo, Texto, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cena1 = Cena("_cenas/amazonia0.jpg").vai()
fala = "Vou pescar no período de defeso, que tem mais peixe"
resposta = "O defeso é para proteger a reprodução, se pescar agora, depois não vai ter"
pescador = Elemento("_ativo/snct/pescador.png", x=200, y=150, texto=fala, cena=cena1)
gabi = Elemento("_ativo/snct/gabi.png", x=450, y=120, texto=resposta, cena=cena1)
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## O agronegócio ganancioso

```python
from vitollino import Cena, Jogo, Texto, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cena1 = Cena("_cenas/desmatamento5.jpg").vai()
fala = "Vou desmatar tudinho e fazer muito pasto para o meu gado"
resposta = "Desgraça! Milhares de árvores arrancadas para dez boizinhos pastarem."
pasto = Cena("_cenas/pastagem.webp")
def vai_pasto(evento=None):
    pasto.vai()
fazendeiro = Elemento("_ativo/snct/fazendeiro.png", x=200, y=150, texto=fala, cena=cena1, foi=vai_pasto)
gabi = Elemento("_ativo/snct/gabi.png", x=450, y=120, texto=resposta, cena=pasto)
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## As queimadas

```python
from vitollino import Sala, Jogo, Texto, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cenas = [f"_cenas/desmatamento{c}.jpg" for c in range(4)]  # imagens das cenas
s = Sala(*cenas)  # encadeia quatro cenas e mostra a cena que está ao norte
s.norte.vai()  # encadeia quatro cenas e mostra a cena que está ao norte

fala= "Tristeza! Estrago! Desperdício! Destruição!".split()
salas = [s.norte, s.leste, s.sul, s.oeste, s.norte]
def queima(c):
    salas[c].vai()
    
pessoas = [Elemento(f"_ativo/snct/{c}.png", x=200, y=150,
                    texto=fala[p], cena=salas[p], foi=lambda x=p:queima(x+1))
           for p, c in enumerate("gabi karaja luiza karaja".split())]  # imagens das cenas

```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## A crise climática

```python
from vitollino import Jogo, Cena
# pegue no guia algo para criar uma cena
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

#### LABASE
[footer](footer.md ':include')