<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# Agentes da ESCOLA
> E, de repente, o rádio tocou</br>
> Cena de cinema </br>

+ Central dos Agentes +
  
    Os Agentes da ESCOLA são chamados para investigar mistérios da Ciência.
  
    Vamos aprender a usar uma planilha com imagens. Aqui podemos criar caminhos alternativos
    para nossa história.
  
    ```python
    """Módulo age.main"""
    from vitollino import Cena, Texto, Jogo, Elemento
    from cenario import Planilha, Paisagens
    Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
  
    class Inicia:
        def __init__(self):
            i_praia, i_mapa = "_ativo/agentes/praia.jpeg", "_ativo/agentes/pergaminho.png"
            mapa_praia = Planilha(i_praia, conta_lado=4.3)
            self.p = p = Paisagens(mapa_praia.j)
            p.norte.vai()
            self.mapa = Elemento(i_mapa, x=200, y=350, h=20, cena=p.norte, vai=self.ve_mapa)
            self.mapa.o, self.cena = 0.2 , p.norte
        def ve_mapa(self, *_):
            m= self.mapa
            m.o, m.x, m.y, m.w, m.h = 1.0, 100, 10, 400, 400
            self.icon(150, 50, "mountain-sun", "Aqui manda procurar uma caverna próxima", self.caverna)
            self.icon(350, 50, "suitcase", "Existe um baú perdido na praia")
            self.icon(150, 270, "mound", "Tem um artefato ancestral escondido em um sambaqui")
            self.icon(350, 270, "church", "Acho que vamos encontrar algo em um templo")
        def icon(self, x, y, ico, diz="", vai=lambda: None, cena=None):
            cena = cena or self.cena
            style = "font-size: 4em; color: peru;"
            icon = Elemento("_ativo/kwarwp/vazio.png", texto=diz, x=x, y=y, cena=cena, foi=vai)
            icon.elt.html = f'<i class="fa fa-{ico}" style="{style}"></i>'
        def caverna(self):
            from age.aventura import Aventura
            Aventura()
    if __name__ == "__main__":
        Inicia()
    ```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

+ Aventuras dos Agentes +
   
    Os agentes descobrem uma caverna com pinturas rupestres.
    Eles vão ter que encontrar pistas nesta caverna.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    """Módulo age.aventura"""
    from vitollino import Cena, Texto, Jogo, Elemento
    from cenario import Planilha, Mapa, Paisagens, Posiciona
    Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
    
    class Aventura:
        def __init__(self):
            i_praia, i_mapa = "_cenas/cavernas.jpg", "_ativo/agentes/pergaminho.png"
            self.p = p = Mapa(i_praia, conta_lado=4.3)
            p = p.salas[0]
            p.norte.vai()
            self.mapa = Elemento(i_mapa, x=60, y=218, h=60, w=50, cena=p.leste, vai=self.ve_mapa)
            self.mapa.o, self.cena = 0.3 , p.norte
 
        def ve_mapa(self, *_):
            m= self.mapa
            m.o, m.x, m.y, m.w, m.h = 1.0, 100, 10, 400, 400
            self.icon(150, 50, "mountain-sun", "Aqui manda procurar uma caverna próxima", self.caverna)
            self.icon(350, 50, "suitcase", "Existe um baú perdido na praia")
            self.icon(150, 270, "mound", "Tem um artefato ancestral escondido em um sambaqui")
            self.icon(350, 270, "church", "Acho que vamos encontrar algo em um templo")
        def icon(self, x, y, ico, diz="", vai=lambda: None, cena=None):
            cena = cena or self.cena
            style = "font-size: 4em; color: peru;"
            icon = Elemento("_ativo/kwarwp/vazio.png", texto=diz, x=x, y=y, cena=cena, foi=vai)
            icon.elt.html = f'<i class="fa fa-{ico}" style="{style}"></i>'
  
        def caverna(self):
            from age.aventura import Aventura
            Aventura()
    if __name__ == "__main__":
        Aventura()    
    ```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

+ As Pistas da Garrafa +
   
    Vejam aonde levam as pistas da garrafa.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

+ Encontrando as Partes +
   
    Vamos procurar as partes da mensagem na garrafa.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

+ Aprendendo com a mensagem +
   
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
   
    Agora sabemos qual era a ideia contida na garrafa.
  
    Agora vamos aprender a usar paisagens e fazer um pequeno roteiro para esta história.
    ```python
    imagem_da_praia = "_ativo/agentes/praia.jpeg"
    mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
    pg = Paisagens(mapa_praia.j[4:])
    p = pg.norte
    p.vai()
    ```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>

#### LABASE
[footer](footer.md ':include')