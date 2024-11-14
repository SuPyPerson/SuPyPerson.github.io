<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# Agentes da ESCOLA
> E, de repente, o rádio tocou</br>
> Cena de cinema </br>

<img src onerror="__did_got__('../../_prog/agente.py')"></img>
<div id="_jogo_" style="position:relative; left:50px">
Aqui está um elemento identificado como '_jogo_'
</div>

+ Central dos Agentes +
 
  <img id="agente_main" src onerror="__widget__(this.id)"/>
 
    Os Agentes da ESCOLA são chamados para investigar mistérios da Ciência.
  
    Vamos aprender a usar uma planilha com imagens
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    p = Paisagem(mapa_praia.j[0]).vai()
    ```

+ Aventuras dos Agentes +
  
  <img id="agente_aventura" src onerror="__widget__(this.id)"/>
 
    Os agentes descobrem uma garrafa perdida na praia.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j)
    p = pg.norte
    p.vai()
    ```

+ As Pistas da Garrafa +
  
  <img id="agente_continua" src onerror="__widget__(this.id)"/>
 
    Vejam aonde levam as pistas da garrafa.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```

+ Encontrando as Partes +
  
  <img id="agente_partes" src onerror="__widget__(this.id)"/>
 
    Vamos procurar as partes da mensagem na garrafa.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```

+ Aprendendo com a mensagem +
  
  <img id="agente_aprende" src onerror="__widget__(this.id)"/>
 
    Vejam aonde levam as pistas da garrafa.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```

+ A Ideia da Garrafa +
  
  <img id="agente_termina" src onerror="__widget__(this.id)"/>
 
    Agora sabemos qual era a ideia contida na garrafa.
  
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