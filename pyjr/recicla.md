<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# Aplicativo Recicla
> E, de repente, o rádio tocou</br>
> Cena de cinema </br>

<img src onerror="__did_got__('../../_prog/recicla.py')"></img>
<div id="_jogo_" style="position:relative; left:50px; min-height: 500px">
Aqui está um elemento identificado como '_jogo_'
</div>

+ Central de Reciclagem +
 
  <img id="recicla_main" src onerror="__widget__(this.id)"/>
 
    Os Agentes da ESCOLA são chamados para investigar lixo abandonado.
  
    Vamos aprender a usar uma planilha com imagens
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    p = Paisagem(mapa_praia.j[0]).vai()
    ```

+ Aventuras Reciclando +
  
  <img id="recicla_aventura" src onerror="__widget__(this.id)"/>
 
    O lixo, que poderia ser reciclado, continua largado, vamos investigar o problema.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j)
    p = pg.norte
    p.vai()
    ```

+ Continua Reciclando +
  
  <img id="recicla_continua" src onerror="__widget__(this.id)"/>
 
    Vejam o que pode ser feito para reciclar o lixo.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```

+ Fase Extra +
  
  <img id="recicla_extra" src onerror="__widget__(this.id)"/>
 
    Vejam o que mais pode ser feito para evitar o descarte indevido.
  
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```

+ Fase Complementar +
  
  <img id="recicla_complemento" src onerror="__widget__(this.id)"/>
 
    Uma ação complementar para evitar o descarte indevido.
  
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```

+ Mundo mais Limpo +
  
  <img id="recicla_termina" src onerror="__widget__(this.id)"/>
 
    Vejam o que pode ser feito para manter o mundo limpo.
  
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