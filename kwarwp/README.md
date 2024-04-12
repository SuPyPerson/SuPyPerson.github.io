<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# Kwarwp - O Início
> E agora para algo totalmente diferente! <br>
> Aprenda Python resolvendo, modificando e criando jogos e desafios. <br>
> Acompanhe a saga do curumim que fugiu da destruição.

<img src onerror="__did_got__('aldeia_0.py')"></img>

+ A Maldade do Caraíba +

  <img id="al0" src onerror="__widget__(this.id)"></img>
  
    Um minuto de silêncio,
    Peço ao amigo leitor
    Pelo massacre expedido
    Que causara grito e dor.
    Chamamos dizimação,
    Esses atos de horror.
    
    Sinto-me envergonhado,
    Caro índio, nesse dia.
    Sei que nenhuma desculpa
    Vai curar a tirania
    Praticada contra ti.
    Teu sangue não silencia.

    **Cordel: Manoel Messias Belizario Neto**


+ Python - O Vaso do Boitatá +

  <img id="al1" src onerror="__widget__(this.id)"></img>

    Curumin em sua fuga encontra perdido no seu caminho o Vaso do Boitatá.
    Este vaso tem a magia do Python, a cobra de fogo.
    Aos poucos ele vai lembrando as lições do seu antigo e agora falecido Pajé.
    Tudo no Python tem um tipo e não se pode misturar os tipos.


+ Python - O Nome das coisas +

  <img id="al2" src onerror="__widget__(this.id)"></img>

    Curumin lembra que ele pode botar nome e apelido em tudo usando Python.
    Para botar um nome basta usar o símbolo *"="*


+ Python - Números e coisas +

  <img id="al3" src onerror="__widget__(this.id)"></img>

    Encontrando e contando os animais pelo caminho.
    * soma: *"+"*
    * subtrai: *"-"*
    * multiplica: *"\*"*
    * divide inteiro: *"//"*


+ Pajé - Seguindo pelo Caminho +

  <img id="al4" src onerror="__widget__(this.id)"></img>

  Caminhe pela cerca até uma oca.
  Use o comando ***for*** do Python.
  Clique no botão executar para mostrar o cenário,
  depois clique no céu para executar um comando passo a passo.
  Clique até que todos os comandos tenham executado.
  Você terá sucesso se o Pajé chegar até sua oca.
    ```python
    for _cada_na_lista in range(0):
      # ponha aqui coisas que se repetem
    ```

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