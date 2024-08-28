<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# Kwarwp - A Trilha
> É pau é pedra, é o fim do caminho <br>
> É um resto de toco, é um pouco sozinho. <br>
> É um caco de vidro, é a vida, é o Sol.

<img src onerror="__did_got__('caminho_0.py')"></img>

+ Pajé - As Toras do Caminho +

  <img id="al5" src onerror="__widget__(this.id)"></img>

  Caminhe pela cerca até uma oca.
  Use o comando ***for*** do Python.
  Clique no botão executar para mostrar o cenário,
  depois clique no céu para executar um comando passo a passo.
  Clique até que todos os comandos tenham executado.
  Você terá sucesso se o Pajé chegar até sua oca.
  Dê um jeito de remover as toras do caminho.
    ```python
    for _cada_na_lista in range(1): # mude o "1" 
      # ponha aqui coisas que se repetem
      self.pega()  # pega o objeto que está na frente
      # bote algo aqui para que funcione
      self.larga()  # larga o objeto em um espaço à frente
      # bote algo aqui para que Pajé siga em seu trajeto
    ```

+ Pajé - O Caminho Sinuoso +

  <img id="al6" src onerror="__widget__(this.id)"></img>

  Caminhe pela cerca até uma oca.
  Use o comando ***while*** do Python.
  Clique no botão executar para mostrar o cenário,
  depois clique no céu para executar um comando passo a passo.
  Clique até que todos os comandos tenham executado.
  Você terá sucesso se o Pajé chegar até sua oca.
    ```python
    while self.olha() == "VAZIO": # enquanto o caminho está livre 
      _ = 0  # troque isso e ponha aqui coisas que se repetem
    ```

+ Pajé - O Caminho Sinuoso Melhorado +

  <img id="al7" src onerror="__widget__(this.id)"></img>

  Caminhe pela cerca até uma oca.
  Use os comando ***def e while*** do Python.
  Podemos definir no Python um conjunto de comandos a serem
  executados juntos. Para isso usamos o comando ***def***.
  No ***def*** daremos um nome a este conjunto de comandos
  que poderão ser chamados por este nome.
  Você terá sucesso se o Pajé chegar até sua oca.
    ```python
    def caminha(self):
      while self.olha() == "VAZIO": # enquanto o caminho está livre 
        _ = 0  # troque isso e ponha aqui coisas que se repetem
    # lá no comando executa faremos assim
    self.caminha()
    self.direita()  # ou self.esquerda
    self.caminha()
    # continue até o Pajé chegar na oca
    ```

+ Pajé - O Caminho Inteligente +

  <img id="al8" src onerror="__widget__(this.id)"></img>

  Caminhe pela cerca até uma oca.
  Use os comando ***def e while*** do Python.
  Podemos definir no Python um conjunto de comandos a serem
  executados juntos. Para isso usamos o comando ***def***.
  Neste ***def*** inteligente, além de caminhar pelo corredor,
  o Pajé fará uma busca para saber por onde deve continuar.
  Teremos então dois comandos ***while*** dentro deste ***def***
  Você terá sucesso se o Pajé chegar até sua oca.
    ```python
    def caminha(self):
      while self.olha() == "VAZIO": # enquanto o caminho está livre 
        _ = 0  # troque isso e ponha aqui coisas que se repetem
      # o Pajé começa tentando seguir à direita do caminho
      self.direita()
      while self.olha() != "VAZIO": # enquanto o caminho não está livre 
        self.esquerda() # se vira para tentar outra direção
    # lá no comando executa faremos assim
    self.caminha()
    self.caminha()
    # continue até o Pajé chegar na oca
    # Outro desafio é trocar estes vários caminhe() por um while!
    ```

#### LABASE
[footer](footer.md ':include')