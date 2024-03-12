<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# O Primeiro Jogo
> Ver teus olhos sempre fixos em mim </br>
> Me fazem recordar dos passos no jardim </br>
> E ao som de tua voz me resta te buscar

<img src onerror="__did_got__('../../_prog/o_jogo0.py')"></img>
<div id="_jogo_" style="position:relative; left:50px; min-height: 500px">
Aqui está um elemento identificado como '_jogo_', onde o jogo vai aparecer.
</div>

+ A Primeira Cena +
 
  <img id="jo0" src onerror="__widget__(this.id)"/>
 
    Vamos aprender aqui a usar o *Vitollino*, uma biblioteca de jogos.
    Primeiro importamos a biblioteca e algumas coisas que ajudam no jogo.
    
    ```python
    from vitollino import Cena, Texto, Jogo
    "O *Jogo* permite ajustar a tela onde se coloca a *Cena*."
    "O *Texto* permite colocar uma mensagem que pula."
    Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
    "No Jogo, o parâmetro *style* define as dimenções do jogo na tela."
    "o parâmetro *did* é o *document id* que define onde o jogo vai surgir."
    ```
    As imagens estão no diretório */_ativo/jardim/*, então vamos 
    usar este texto como gabarito para buscá-las. 
    O comando *format* vai substituir o nome das imagens no local
    demarcado por um *{}*
    ```python
    japones, relogio = local.format("japones"), local.format("relogio")
    "No início da linha *japones* e *relogio* sã apelidos que criamos"
    ```
    Estes apelidos, japones, relogio são usados
    para substituir os nomes mais longos: */_ativo/jardim/japones.jpg*, etc.
    
    Por fim temos dois comandos, um com uma *Cena* e o outro com um *Texto*
    Quando adicionamos o *.vai()* depois da Cena e do Texto
    queremos que eles apareçam.
    ```python
    cena = Cena(japones).vai()
    "japones aqui diz que a imagem da cena á aquela da figura japones.jpg"
    Texto(cena, "Olá, Vamos construir o Jardim Radical!").vai()
    "No texto, o apelido *cena* diz a cena que vai mostrar o texto que é colocado após a vírgula"
    ```
+ Mais Cenas no Jogo +
 
  <img id="jo1" src onerror="__widget__(this.id)"/>

  Vamos criar mais cenas e criar uma navegação entre elas.
  A *Cena* tem parâmetros como *esquerda* e *direita*.
  Neles se pode colocar outras cenas, criando uma ligação.
  Quando se passa o mouse perto das bordas, uma seta aparece
  e voce pode clicar para ir à cena que está à direita ou esquerda.
  ```python
  cena_japones = Cena(japones)
  "A *cena_japones* está sozinha, pois não havia outra cena acima."
  cena_relogio = Cena(relogio, esquerda=cena_japones)
  "A *cena_relogio* pode ter um vizinho, pois a cena_japones veio antes."
  ```
  Como ficamos com o problema da galinha e o ovo, vamos dar um jeito.
  A *Cena* tem propriedades como *esquerda* e *direita*.
  Nelas se pode atribuir outras cenas, resolvendo o que faltava.
  ```python
  cena_relogio.direita = cena_mirante
  "Agora o relogio que só tinha esquerda, pode receber cena à direita"
  cena_japones.esquerda = cena_mirante
  "Agora o japones, que não tinah nada, pode receber cena à esquerda"
  cena_japones.direita = cena_relogio
  "Agora o japones pode receber cena à direita também"
  ```
  Olhe com atenção o código e use os exemplos para anexar o mirante.
  Voce vai ter que atribuir de novo alguns vizinhos para fazer isto.
  Aproveite que as otras cenas estão acima do mirante e adicione
  os parâmetros direita e esquerda, formando a vizinhança do mirante.
  Veja se você consegue agora rodar pela direita ou esquerda, 
  incluindo uma passagem pelo mirante.

+ Criando Salas no Jogo +
 
  <img id="jo2" src onerror="__widget__(this.id)"/>

  Vamos facilitar a criação de cenas navegáveis com a *Sala*.
  A *Sala* tem proriedades *norte, oeste, sul e leste* que são
  as cenas que estão nesta posição.
  Na *Cena*, o parâmetro *meio* indica a cena quando se navega em frente.
  A seta do meio vai aparecer na borda do topo da imagem.
  Procure ligar as duas salas, fazendo o meio do norte de uma sala
  levar à cena norte da outra. Faça depois o caminho inverso, ligando
  o meio do sul ligar no sul da outra sala.
  ```python
  cenas = "japones relogio mirante tomjobim".split()
  """a chamada *split* recorta o texto nos espaços, retornando
  # a lista de textos: *["japones", "relogio", "mirante", "tomjobim"]*
  """
  jardim = Sala(*[f"/_ativo/jardim/{cena}.jpg" for cena in cenas])
  """Aqui a lista de cenas é percorrida com o comando *[$1 for $2 in $3]*
  o *$3* é a lista ser percorrida. O $2 é valor corrente da lista.
  O $3 é executado para cada valor da lista.
  O * na frente do *[]* separa a lista em parâmetros a serem passados para *Sala*
  """
  ```

#### LABASE
[footer](footer.md ':include')