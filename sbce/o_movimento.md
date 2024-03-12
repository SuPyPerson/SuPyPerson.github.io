<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# As Atividades
> We watch in reverence </br>
> As Narcissus is turned into a flower </br>
> (A flower?)


<img src onerror="__did_got__('../../_prog/o_jogo0.py')"></img>
<div id="_jogo_" style="position:relative; left:50px; min-height: 500px">
Aqui está um elemento identificado como '_jogo_'
</div>

+ E Narciso se Torna uma Flor +
 
  <img id="jo5" src onerror="__widget__(this.id)"/>
 
  Narciso sai da presença do outros e vai se olhar no lago.
  Para isso definimos uma ação em python usando *def* (definição).
  ```python
  def narciso_vai(*_):
      """Esse def vai fazer o Narciso ir para o lago"""
      lago = jardim.sul.vai()
      "fazemos aqui o sul do jardim aparecer, enviando *vai()* para ele."
      narciso.entra(lago)
      "o elemento narciso move para o lago."
      narciso.vai = lambda _: None
      "o *lambda _: None* é uma ação vazia. O *narciso.vai()* agora nada faz."

  falou = Texto(cena, "Deu para mim, já vou", foi=narciso_vai).vai
  narciso.vai = falou
  ```

![Em Construção](../_media/em_construcao.png)


#### LABASE
[footer](footer.md ':include')