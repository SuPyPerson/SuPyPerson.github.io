
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
Agora vamos aprender a usar paisagens e conectar  uma paisagem na próxima.
```python
from vitollino import Cena, Jogo, Texto
from cenario import Planilha, Paisagens
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
pg = Paisagens(mapa_praia.j)
p = pg.norte
p.vai()
Texto(pg.norte, "Temos uma bela praia Aqui").vai()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
### Descreve Paisagens
Agora vamos aprender a usar paisagens e fazer uma pequena narrativa para esta história.
```python
from vitollino import Cena, Jogo, Texto
from cenario import Planilha, Paisagens
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
pg = Paisagens(mapa_praia.j)
n, l, s, o = pg.cenas  # obtém as quatro cenas das paisagens
def descreve(a_cena, o_texto):  # atribui um texto para cada cena
    a_cena.foi = Texto(a_cena, o_texto).vai  # o gatilho foi ativa ao entrar
    '''engaja no gatilho de entrada da cena a ativação "vai" do texto'''
for cena, texto in zip([n, l, s, o], "norte leste sul oeste".split()):
    descreve(cena, f"Temos uma bela praia ao {texto}")
n.vai()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Atores e Objetos
<a name="vi-ato-"></a>
A biblioteca fornece as classe Elemento que permite incluir personagens e artefatos em cena.
Permite também movimentar e criar animações limitadas.
Personagens podem navegar entre as diversas cenas do cenário e reagir a interações do jogador.
No *Elemento* usamos os parâmetros *x, y, h* para definir a posição e tamanho.
O primeiro parâmetro é a imagem do elemento e *cena* determina a cena onde fica.
O parâmetro texto, quando existe, determina a fala decorrente do click no elemento.
```python
from vitollino import Cena, Jogo, Elemento
from cenario import Planilha, Paisagens
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
pg = Paisagens(mapa_praia.j)
n, l, s, o = pg.cenas  # obtém as quatro cenas das paisagens
cena = n
robert, maria, rosa = [f"/_ativo/{ator}.png" for ator in "robert maria rosalinda".split()]
robert = Elemento(robert, x=50, y=200, h=200, cena=cena, texto="O rato cientista")
maria = Elemento(maria, x=250, y=200, h=200, cena=cena, texto="A estudante curiosa")
rosa = Elemento(rosa, x=450, y=200, h=200, cena=cena, texto="A cientisata famosa")
cena.vai()
"Experimente mudar a posição e tamanho dos personagens"
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Falas e Roteiros
<a name="vi-fal-"></a>
Existem classes para criar falas, questionários de múltipla escolha que podem ser usados para criar uma novela gráfica.
Um *Roteiro* define um diálogo entre vários personagens que podem interagir em uma contação de história grupal.
O *Ator* define um elemento, o nome do personagem e a fração do ícone que aparece onde *1.0* é o corpo todo e *0.5* só a metade.
O último parâmetro é onde o ícone dele aparece sobre a fala: *A.e, A.m e A.d*, esquerda, meio ou direita.
Uma *Fala* determina o ator que fala, o texto que ele fala, quem é o próximo e a acão que acontece.
```python
from vitollino import Jogo, Elemento
from vitollino import Roteiro, Ator, Fala, A
from cenario import Planilha, Paisagem
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
a_cena = Paisagem(mapa_praia.j[0])
a_cena.vai()
ros = Elemento("_ativo/rosalinda.png", x=400, y=250, cena=a_cena)
mar = Elemento("_ativo/maria.png", x=150, y=250, cena=a_cena)
elenco = (Ator(ros, "Rosalinda", 0.4, A.d),
          Ator(mar, "Maria", 0.4, A.e))
falas = [
    Fala(ros, "Os pescadores dizem que algo estranho acontece aqui", mar, None),
    Fala(mar, "Temos que investigar o que está acontecendo", ros, None),
]
Roteiro(a_cena, falas, elenco)
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

[footer](footer.md ':include')