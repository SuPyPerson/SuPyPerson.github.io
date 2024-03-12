<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# Os Personagens
> Não! Eu só vou se for pra ver </br>
> Uma estrela aparecer </br>
> Na manhã de um novo amor


<img src onerror="__did_got__('../../_prog/o_jogo0.py')"></img>
<div id="_jogo_" style="position:relative; left:50px; min-height: 500px">
Aqui está um elemento identificado como '_jogo_'
</div>

+ O Elenco, Os Habitantes do Jardim +
 
  <img id="jo3" src onerror="__widget__(this.id)"/>
 
  Agora vamos povoar este jardim com estátuas falantes.
  Para isso vamos usar o *Elemento*, que coloca coisas na cena.
  ```python
  cenas = "japones relogio mirante tomjobim".split()
  "Vamos usar a sala do exemplo anterior"
  jardim = Sala(*[f"/_ativo/jardim/{cena}.jpg" for cena in cenas])
  cena = jardim.sul.vai()
  "Escolhemos a cena sul, o mirante, para ser a cena inicial"
  ```
  Vamos usar o construtor de lista dinâmica *[$1 for $2 in $3]*
  para formatar o endereço correto da imagem a partir da lista *personagens*.
  ```python
  pessoa = "/_ativo/jardim/{}.png"  # este {} vai ser substituído pelo format
  personagens = "narciso", "ossanha", "tetis"
  narciso, ossanha, tetis = [pessoa.format(personagem) for personagem in personagens]
  ```
  No *Elemento* usamos os parâmetros *x, y, h* para definir a posição e tamanho.
  O primeiro parâmetro é a imagem do elemento e *cena* determina a cena onde fica.
  O parâmetro texto, quando existe, determina a fala decorrente do click no elemento.
  ```python
  tetis = Elemento(tetis, x=50, y=300, h=200, cena=cena, texto="A Fecundidade")
  ossanha = Elemento(ossanha, x=250, y=300, h=200, cena=cena, texto="O Curandeiro")
  narciso = Elemento(narciso, x=450, y=300, h=200, cena=cena, texto="O Orgulhoso")
  "Experimente mudar a posição e tamanho dos personagens"
  ```

+ O Diálogo dos Habitantes +
 
  <img id="jo4" src onerror="__widget__(this.id)"/>
 
  Os milenares habitantes estão em uma discussão acalorada.
  Vamos usar o *Roteiro*, para definir como será este diálogo.
  Vamos usar o construtor de lista dinâmica *[$1 for $2 in $3]*
  para formatar cada *Elemento* a partir da lista *personagens*.
  ```python
  local = "/_ativo/jardim/"  
  personagens = ("narciso", 450), ("ossanha", 250), ("tetis", 50)
  "Personagens agora são pares ordenados com o nome e a posição x dos personagens"
  narciso, ossanha, tetis = [
    Elemento(f"{local}{nome}.png", x=x, y=300, h=200, cena=cena)
    for nome, x in personagens]
  "Neste *[$1 for $2 in $3]*, $1 é o elemento que recebe os parâmetros de $2"

  ```
  Para isso teremos que importar as classes que ajudam no diálogo.
  + **Roteiro:** Vai executar o diálogo na *cena*, dado o *elenco* e as *falas*.
  + **Ator:** Definido por um *elemento*, *nome*, *proporção* e *posição*.
  + **Fala:** Define um *autor*, o *texto* o *proximo* falante e uma *ação*.
  + **A:** É usado para definir a *posição* do ícone do autor no topo da fala.
  + **A.e, A.m, A.d:** Coloca o ícone na esquerda, meio ou direita da fala.

  ```python
  from vitollino import Roteiro, Ator, Fala, A
  # bla, bla, bla ...
  elenco = (Ator(tetis, "Tetis", 0.4, A.e), Ator(ossanha, "Ossanha", 0.4, A.m),
          Ator(narciso, "Narciso", 0.4, A.d))
  "O ícone de Tetis surgirá à esquerda, Ossanha ao meio e Narciso à direita"
  ```


#### LABASE
[footer](footer.md ':include')