
# Guia de Construção de Jogos
## As cinco fases de pedagogia neurocientífica
Nesta fase temos um conjunto de propostas e protótipos construídos pelos participantes.
Na reunião em pé vamos dividir a turma em quatro grupos e tentar fazer um produto mínimo com quatro conceitos.
Os grupos vão construir “tomadas” relativas ao tema escolhido dentre Matemática, Ciência, Linguagem e História.
Cada tema vai ser divido em cerca de quatro tarefas que serão distribuídas entre os participantes.
Cada equipe produzirá o seu próprio jogo e plataforma já dispõe de uma engenharia para unir as partes distribuídas em um único executável.

## Repensado o “StoryBoard”
Uma nova maquete de localidades será construída segundo os requisitos do jogo escolhido para cada equipe.
No guia dos agentes, os personagens Luiza, Allyce e Ramon se juntam a Kayke para protagonizar as quatro missões tema dos jogos.
Agora vamos usar a paisagens e fazer uma pequena planilha gráfica para esta história.
```python
from vitollino import Cena, Jogo, Texto, Cursor, Elemento, Dragger, Point
from cenario import Planilha, Paisagens, Posiciona
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
class Cenario:
    def __init__(self, azimute=0, lote=0):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        self.pg = pg = Paisagens(mapa_praia.j[lote:])
        self.cena = pg.cenas[azimute]  # obtém as quatro cenas das paisagens
    def marca(self, marcador="_ativo/marcador.png"):
        e = "_ativo/marcador.png"
        a = Posiciona(marcador, cena=self.cena)
        # um marcador 📍 que você pode arrastar
        return self
    def vai(self, azimute=None):
        self.cena = self.pg.cenas[azimute] if azimute else self.cena
        self.cena.vai()
        return self
if __name__ == "__main__":
    Cenario().vai().marca()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Definindo a Conversa
Como agora o jogo é feito em equipe, cada participante deve se responsabilizar
por um módulo que define uma ou mais tomadas de cena.
Segue então a descrição de um documento comum que define como os módulos
se entrelaçam e como cada um oferece os pontos de chamada para compor a unidade final.

```python
from vitollino import Jogo, Elemento, Texto
from cenario import Planilha, Paisagens
from jogos import Sequencia
JOGO = Jogo(style=dict(height="450px", width="600px"), did="_jogo_")
class TomadaLiteratura:
    def __init__(self, jogo, cenario=None):
        self.jogo = jogo
        self.mapa = Elemento("_ativo/agentes/diagrama_sol.png", x=4, y=160, w=290, h=290)
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        self.n = n = cenario or Paisagens(mapa_praia.j).norte
        fala = "Na garrafa tinha um pergaminho, mas ele está em tiras, tenho que ajeitar!"
        maria = Elemento("_ativo/maria.png", texto=fala, x=500, y=200, cena=n, foi=self.montar)
    def montou(self):
        return Texto(self.n, "É a Canção do Exílio do Gonçalves Dias! Mas tem algo atrás!",
                  foi=lambda: self.mapa.entra(self.n))
    def montar(self):
        img = "_ativo/agentes/exilio.png"
        poema = Sequencia(self.jogo, img, self.n, w=250, h=250, x=10, y=10, dw=2, dh=2,
            venceu=self.montou(), dim=(10, 180, 2))
        '''Monta o jogo da Sequência , para ordenar um conjunto de tiras'''
    def vai(self):
        self.n.vai()
        return self
if __name__ == "__main__":
    TomadaLiteratura(JOGO).vai()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Encapsulando uma Tomada de Cena
Em cada módulo, desenvolvido individualmente por cada membro do grupo,
será construído um conjunto de tomadas de cena e ações utilitárias pertinentes
àqueles componentes da trama. No “Guia do Agente” existem exemplos e objetos já
encapsulados com as interações que eles podem ter com o jogo, desenhados para a construção do “Caso do Relógio”.

```python
from vitollino import Jogo, Elemento
from cenario import Planilha, Paisagens
from jogos import Associa
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
class TomadaCiente:
    def __init__(self, cenario=None):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        self.paisagens = Paisagens(mapa_praia.j)
        self.n = n = cenario or self.paisagens.norte
        nomes = "Equador,eixo da terra,gnômon,observador,latitude,horizonte"
        self.nomes = {k[0]: k for k in nomes.split(",")}
        self.maria = Elemento("_ativo/maria.png", x=500, y=200, cena=n)
        self.mapa = Elemento("_ativo/agentes/diagrama_sol.png", x=120, y=10, w=400, h=400, cena=n)
    def associa(self):
        n, nomes = self.n, self.nomes
        associa = Associa(n, caixa=300, borda=20, acertos=3)
        '''Monta o jogo da associação, associando os nomes abaixo com as lacunas'''
        associa.nome(nome=nomes["E"], tit=0, x=185, y=225)
        associa.nome(nome=nomes["e"], tit=1, x=331, y=276)
        associa.nome(nome=nomes["g"], tit=2, x=291, y=35)
        # complete o enigma posicionando todos os nomes no diagrama
        return self
    def vai(self):
        self.n.vai()
        return self
if __name__ == "__main__":
    TomadaCiente().associa().vai()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Montando a Criatura
Neste quarto final o jogo do grupo é montado em um módulo de integração
que designa como as partes se encaixam. Basicamente este módulo importa
os módulos construídos pelos participantes e conecta as cenas usando uma classe Labirinto ou Mapa.

```python
from vitollino import Jogo
JOGO = Jogo(style=dict(height="450px", width="600px"), did="_jogo_")
exec(__use__("_refina_rep"))  # importa o módulo Repensando o Storyboard
exec(__use__("_refina_def"))
exec(__use__("_refina_enc"))
c = Cenario(2, 4).vai()
TomadaLiteratura(JOGO, c.cena).vai()
TomadaCiente(c.vai(3).cena).vai()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

[footer](footer.md ':include')