
# Exploração - Olhando Horizontes

A fase começa com uma reunião em pé de cinco minutos onde são exploradas as expectativas e propostas dos participantes. Nos quartos teremos uma visão rápida da linguagem Python e da biblioteca Vitollino criada para facilitar a criação de jogos usando esta metodologia.

## Aprenda Python em Dez minutos
<a name="py-ten-"></a>
- Korokithakis [2018] desenvolveu este material para dar um impulso inicial para o aprendiz da linguagem Python. A versão do curso é mais enxuta e foca nas necessidades do desenvolvimento de games.
### A mata atlântica

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
### A caatinga

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

## Criando cenários com Vitollino
<a name="vi-cen-"></a>
- A biblioteca Vitollino é parte integrante da plataforma e provê um conjunto de facilidades para o desenvolvimento de jogos. O cenário é criado a partir das classes Cena, Sala, Labirinto e Mapa. Imagens prontas estão disponíveis na biblioteca do “Guia do Agente”.

Os Agentes da ESCOLA são chamados para investigar uma mensagem encontrada numa garrafa.
### A Praia
Vamos aprender a usar uma planilha com imagens
```python
from vitollino import Cena, Jogo
from cenario import Planilha, Paisagem
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
p = Paisagem(mapa_praia.j[0]).vai()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

A mensagem fala sobre um baú perdido na praia.
### As Paisagens
Agora vamos aprender a usar paisagens e fazer uma pequena narrativa para esta história.
```python
from vitollino import Cena, Jogo
from cenario import Planilha, Paisagem
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
pg = Paisagens(mapa_praia.j)
p = pg.norte
p.vai()
Texto(pg.norte, "Temos uma bela praia Aqui").vai()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Atores e Objetos
<a name="vi-ato-"></a>
- A biblioteca fornece as classe Elemento e Inventário que permitem incluir personagens e artefatos em cena. Permite também movimentar e criar animações limitadas. Personagens podem navegar entre as diversas cenas do cenário e reagir a interações do jogador. Objetos podem ser colocados no inventário e podem ser programados para interagir com outros objetos.

## Falas e Roteiros
<a name="vi-fal-"></a>
- Existem classes para criar falas, questionários de múltipla escolha que podem ser usados para criar uma novela gráfica. Um roteiro pode definir um diálogo entre vários personagens que podem interagir em uma contação de história grupal.

[footer](footer.md ':include')