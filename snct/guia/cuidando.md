<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# O Agente da SME - Cuidando dos Biomas
> E agora para algo totalmente diferente! <br>
> Aprenda Python resolvendo, modificando e criando jogos e desafios. <br>

Vamos criar uma ação para cuidar dos biomas. Escolha uma opção de jogo

## Protegendo a fauna

```python
from vitollino import Cena, Jogo, Elemento, Texto
from jogos import Swap
j = Jogo(style=dict(height="450px", width="600px"), did="_jogo_") #.z()
a_cena = Cena("_cenas/amazonia1.jpg").vai()
fala = "Precisamos desarmar estas arapucas para preservar a fauna!!."
Elemento("_ativo/rosalinda.png", x=300, y=300, texto=fala, cena=a_cena)
class Arapuca:
    def __init__(self, x, y, h, v):
        self.h, self.v = h, v
        abafa = "Resolva o quebra-cabeça para desarmar a arapuca"
        self.arapuca = Elemento("_ativo/snct/arapuca.png",tit="arapuca",
            x=x, texto=abafa, y=y, cena=a_cena, foi=self.desarma)

    def desarma(self, *_):
        self.problema = Swap(j, "_ativo/snct/arapuca.png",
        a_cena, 300, 300, 200, 40, self.h, self.v, venceu=self)
    def vai(self):
        Texto(a_cena, "Você desarmou esta arapuca", foi=self.some).vai()
    def some(self):
        vazia = Cena()
        self.arapuca.entra(vazia)
        [peca.entra(vazia) for peca in self.problema.pecas]
        
Arapuca(100, 340, 3, 2)
Arapuca(300, 180, 3, 3)
Arapuca(400, 350, 3, 4)
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Protegendo a flora

```python
# procure dicas no Guia
from vitollino import Cena, Jogo, Elemento, Texto
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena = Cena("_cenas/cerrado1.jpg").vai()
fala = "Preciso usar um abafador para conter este fogo!."
Elemento("_ativo/rosalinda.png", x=300, y=300, texto=fala, cena=a_cena)
abafa = "Arraste até o fogo para abafar"
abafa = Elemento("_ativo/snct/abafador.png",tit="abafador",
x=100, drag=True, texto=abafa, y=350, cena=a_cena)
class Fogo:
    def __init__(self):
        self.fogo = Elemento("_cenas/fogo.png",w=500, x=50, y=150,
        cena=a_cena, drop=dict(abafador=self.apaga))
        self.altura = 1.0
    def apaga(self, ev, nome):
        self.altura -= 0.2
        if self.altura < 0.4:
            self.fogo.entra(Cena())  # O fogo sai de cena
            Texto(a_cena, "Ufa o fogo apagou!").vai()
        else:
            self.fogo.o = self.altura
        
Fogo()
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Protegendo o ambiente

```python
from vitollino import Jogo, Cena
# pegue no guia algo para criar uma cena
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Protegendo a água

```python
from vitollino import Jogo, Cena
# pegue no guia algo para criar uma cena
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

## Protegendo a atmosfera

```python
from vitollino import Jogo, Cena
# pegue no guia algo para criar uma cena
```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

#### LABASE
[footer](footer.md ':include')