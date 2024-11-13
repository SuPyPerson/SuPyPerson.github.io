<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# Aplicativo Help Pet
> E, de repente, o rádio tocou</br>
> Cena de cinema </br>

<img src onerror="__did_got__('../../_prog/help_pet.py')"></img>
<div id="_jogo_" style="position:relative; left:50px; min-height: 500px">
Aqui está um elemento identificado como '_jogo_'
</div>

+ Central Help Pet +
 
  <img id="help-pet_main" src onerror="__widget__(this.id)"/>
 
    Os Agentes da ESCOLA são chamados para investigar animais em perigo.
  
    Vamos aprender a usar uma planilha com imagens
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    p = Paisagem(mapa_praia.j[0]).vai()
    ```

+ Aventuras com Pets +
  
  <img id="help-pet_aventura" src onerror="__widget__(this.id)"/>
 
    Os pets correm perigo, vamos investigar o problema.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j)
    p = pg.norte
    p.vai()
    ```

+ Resgatando os Pets +
  
  <img id="help-pet_continua" src onerror="__widget__(this.id)"/>
 
    Vejam o que pode ser feito para resgatar os pets.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```

+ Pets em Segurança +
  
  <img id="help-pet_termina" src onerror="__widget__(this.id)"/>
 
    Vejam o que pode ser feito para manter os pets seguros.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```

#### LABASE
[footer](footer.md ':include')