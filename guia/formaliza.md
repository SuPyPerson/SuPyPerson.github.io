
# Guia de Construção de Jogos
As cinco fases de pedagogia neurocientífica......

Seguindo o Guia do Desenvolvedor temos a aventura “Os Agentes da J.A.I.E - O Caso do Relógio”.
Na reunião em pé discutimos a diretriz conceitual da franquia “Os Agentes”.
Neste caso, os agentes vão investigar uma mensagem numa garrafa achada por pescadores numa praia remota.
Será pensado um mapa das “tomadas de cena” dentro do cenário e o “corte do diretor” para este episódio.
Nesta fase todos trabalham individualmente e tentam construir uma proposta para o jogo.

## O Cenário da Praia
Nesta praia remota temos quatro localizações que podem ser escolhidas para criar encontros com personagens
e posicionar artefatos importantes para as missões. Os pontos-chave podem ser marcados por uma imagem
genérica com uma legenda explicativa. Esta é uma forma de criar uma “StoryBoard” interativa.
### Preparando a História
Agora vamos usar a paisagens e fazer uma pequena planilha gráfica para esta história.
```python
from vitollino import Cena, Jogo, Texto, Cursor, Elemento, Dragger, Point
from cenario import Planilha, Paisagens, Posiciona
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
pg = Paisagens(mapa_praia.j)
n, l, s, o = pg.cenas  # obtém as quatro cenas das paisagens
n.vai()
e = "_ativo/marcador.png"
a = Posiciona(e, cena=n)  # um marcador 📍 que você pode arrastar

```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Os Agentes e suas Missões
Temos no guia um conjunto de agentes e figurantes que podem fornecer missões secundárias.
Aqui vamos experimentar a criação de minijogos já disponíveis na biblioteca Vitollino.

## A Missão Literária e Histórica 
O nosso agente erudito Kayke se entusiasma ao ver o conteúdo da mensagem na garrafa.
Na mensagem existe um texto e um mapa para encontrar um baú contendo instruções e
peças para a montagem de um relógio do sol. Kayke se arvora a contar a importância
da medição do tempo para a humanidade desde a era Neolítica.
Enquanto todos tentam entender a história do Kayke em sua linguagem pomposa,
Allyce, em sua imaginação, já está vestida em uma pele mal costurada,
lança em punho, caça um fantasioso mamute e se põe a compor uma ode ao seu feito.
### Mensagem na Garrafa
Na mensagem da garrafa tinha um diagrama ilustrativo de como montar o relógio de sol.

```python
from vitollino import Jogo, Elemento, Texto
from cenario import Planilha, Paisagens
from jogos import Sequencia
def montar():
    poema = Sequencia(j, img, n, w=250, h=250, x=10, y=10, dw=2, dh=2,
        venceu=montou, dim=(10, 180, 2))
    '''Monta o jogo da Sequência , para ordenar um conjunto de tiras'''
j = Jogo(style=dict(height="450px", width="600px"), did="_jogo_")
mapa = Elemento("_ativo/agentes/diagrama_sol.png", x=4, y=160, w=290, h=290)
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
n = Paisagens(mapa_praia.j).norte
montou = Texto(n, "É a Canção do Exílio do Gonçalves Dias! Mas tem algo atrás!",
          foi=lambda: mapa.entra(n))
n.vai()
fala = "Na garrafa tinha um pergaminho, mas ele está em tiras, tenho que ajeitar!"
maria = Elemento("_ativo/maria.png", texto=fala, x=500, y=200, cena=n, foi=montar)
img = "_ativo/agentes/exilio.png"
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
## A Missão Científica e Matemática
Vamos criar um esquete que envolva o aprendizado de algum conhecimento científico e matemático.
No “Caso do Relógio” temos os conceitos de movimentos do planeta terra,
a conservação do momento angular (1ª lei de Newton). Na matemática temos as coordenadas cartesianas
para a interpretação dos mapas e o cálculo e divisão do círculo em setores (as latitudes da terra).
### Terra Rodando
A terra roda e isto se reflete no relógio de sol, que projeta sua sombra indicando as horas.
```python
from vitollino import Cena, Jogo, Texto, Cursor, Elemento, Dragger, Point
from cenario import Planilha, Paisagens, Posiciona
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
pg = Paisagens(mapa_praia.j)
n, l, s, o = pg.cenas  # obtém as quatro cenas das paisagens
n.vai()
coisas = "relogio.png terra_girando.gif fala.png".split()
r, t, f = [f"_ativo/agentes/{im}" for im in coisas]
m = "_ativo/maria.png"
fala = "O relógio de sol funciona com a rotação da terra"
explica = "explique algo aqui"
def foi():
    Elemento(f, cena=n, x=400, y=100, w=200, h=200)
    Elemento(t, cena=n, x=450, y=150, texto=explica)
maria = Elemento(m, cena=n, x=350, y=300, texto=fala, foi=foi)
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>
### Ajustando o relógio
Na mensagem da garrafa tinha um diagrama ilustrativo de como montar o relógio de sol.

```python
from vitollino import Jogo, Elemento
from cenario import Planilha, Paisagens
from jogos import Associa
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
imagem_da_praia = "_ativo/agentes/praia.jpeg"
mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
n = Paisagens(mapa_praia.j).norte
n.vai()
nomes = {k[0]: k for k in "Equador,eixo da terra,gnômon,observador,latitude,horizonte".split(",")}
maria = Elemento("_ativo/maria.png", x=500, y=200, cena=n)
mapa = Elemento("_ativo/agentes/diagrama_sol.png", x=120, y=10, w=400, h=400, cena=n)
associa = Associa(n, caixa=300, borda=20, acertos=3)
'''Monta o jogo da associação, associando os nomes abaixo com as lacunas'''
associa.nome(nome=nomes["E"], tit=0, x=185, y=225)
associa.nome(nome=nomes["e"], tit=1, x=331, y=276)
associa.nome(nome=nomes["g"], tit=2, x=291, y=35)
# complete o enigma posicionando todos os nomes no diagrama
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

[footer](footer.md ':include')
