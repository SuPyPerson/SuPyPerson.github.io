<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# Guia do Agente da SME - Conhecendo os Biomas
> E agora para algo totalmente diferente! <br>
> Aprenda Python resolvendo, modificando e criando jogos e desafios. <br>

## A floresta Amazônica

Vamos fazer um jogo com animais da amazônia

```python
bichos = "escolha um bicho da amazônia: a-anta, b-urso, c-capivara, d-tatu."
bicho = input(bichos)
while bicho not in "acd":
    bicho = input(bichos)
input("você acertou")
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## A mata atlântica

Vamos fazer um jogo com animais da mata atlântica

```python
bichos = dict(a="quati", b="pinguim", c="coruja", d="sucuri")
escolha = "escolha um bicho da mata atlântica: " + str(bichos)
bicho = input(escolha)
while bicho not in "ac":
    pergunta = f"{bichos[bicho]} não é, "+escolha
    bicho = input(pergunta)
input("você acertou" if bicho else "você desistiu")
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## A caatinga

Vamos fazer um jogo com animais da caatinga

```python
bichos = "escreva certo um animal da caatinga: comó, bamgá, caracrá, amerise."
bicho = input(bichos)
while bicho not in "carcará gambá seriema mocó":
    pergunta = f"{bicho} não é, "+ bichos
    bicho = input(pergunta)
input(f"você acertou, {bicho} é um animal da caatinga" if bicho else "você desistiu")
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## O pantanal

Vamos fazer um jogo com animais do pantanal

```python
bichos = "escolha um bicho do pantanal: a-onça pintada, b-ariranha, c-arara azul."
bicho = input(bichos)
while bicho not in "c":
    bicho = input(bichos)
input("você acertou")
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## O cerrado

Vamos fazer um jogo com animais do cerrado

```python
bichos = "escolha um bicho do cerrado: a-lontra, b-tatu-canastra, c-tamanduà, d-catitu, e-macaco-prego"
bicho = input(bichos)
while bicho not in "a":
    bicho = input(bichos)
input("você acertou")
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## O pampa

Vamos fazer um jogo com animais do pampa

```python
bichos = "escolha um bicho do pampa: a-tachã, b-tuco-tuco, c-sapinho de barriga vermelha, d-beija flor da barba azul."
bicho = input(bichos)
while bicho not in "d":
    bicho = input(bichos)
input("você acertou")
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## A fauna

- PANTANAL- ONÇA PINTADA, ARIRANHA, ARARA AZUL GRANDE.
- AMAZÔNIA- ANTA, LOBO GUARÁ, CAPIVARA, TATU.
- MATA ATLÂNTICA- QUATI, MICO-LEÃO-DOURADO, CORUJA.
- CAATINGA- ONÇA-PARDA, TATU-BOLA, GAMBÁ, MOCÓ.
- PAMPA- TACHÃ, TUCO-TUCO, SAPINHO DE BARRIGA VERMELHA, BEIJA FLOR DA BARBA AZUL.
- CERRADO- LONTRA, TATU-CANASTRA, TAMANDUÁ, CAITITU, MACACO-PREGO.

#### LABASE
[footer](footer.md ':include')