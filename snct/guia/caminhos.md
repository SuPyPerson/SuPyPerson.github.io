<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# Guia do Agente da SNCT - Trilhando os Caminhos
> E agora para algo totalmente diferente! <br>
> Aprenda Python resolvendo, modificando e criando jogos e desafios. <br>

## A floresta Amazônica

Vamos fazer um jogo com cenário da amazônia. Tem duas cenas e uma navega para a outra

```python
from vitollino import Cena, Jogo
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cena1 = Cena("_cenas/Amazonia.jpeg").vai()
cena2 = Cena("_cenas/amazonia.jpg", direita=cena1, esquerda=cena1).vai()
cena1.direita = cena1.esquerda = cena2
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## A mata atlântica

Vamos fazer um jogo com cenário da mata atlântica. Tem três cenas e uma navega para a outra circularmente

```python
from vitollino import Jogo, Cena
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cena1 = Cena("_cenas/mata-atlantica.jpg")
cena2 = Cena("_cenas/mata-atlantica3.jpg", esquerda=cena1)
cena3 = Cena("_cenas/mata-atlantica-1.jpg", direita=cena1, esquerda=cena2).vai()
cena2.direita = cena1.esquerda = cena3
cena1.direita = cena2
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## A caatinga

Vamos fazer um jogo com cenário da caatinga. Tem quatro cenas e uma navega para a outra circularmente

```python
from vitollino import Jogo, Sala
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cenas = [f"_cenas/caatinga{c}.jpg" for c in range(1,5)]  # imagens das cenas
Sala(*cenas).norte.vai()  # encadeia quatro cenas e mostra a cena que está ao norte
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## O pantanal

Vamos fazer um jogo com cenário do pantanal. Encadeia duas salas e navega uma para outra.

```python
from vitollino import Jogo, Sala, Labirinto
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cenas_c = [f"_cenas/caatinga{c}.jpg" for c in range(1,5)]
sala_c = Sala(*cenas_c)
cenas_p = [f"_cenas/pantanal{c}.jpg" for c in range(1,5)]
sala_p = Sala(*cenas_p)
lb = Labirinto(sala_c, sala_p, sala_p, sala_p, sala_p)
sala_p.norte.vai()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

#### LABASE
[footer](footer.md ':include')