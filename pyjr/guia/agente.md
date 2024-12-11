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
            i_praia, self.pr = "_ativo/agentes/praia.jpeg", "_ativo/agentes/pergaminho.png"
            mapa_praia = Planilha(i_praia, conta_lado=4.3)
            self.p = p = Paisagens(mapa_praia.j)
            p.norte.vai()
            self.cena = p.norte
            self.alternativas()
        def alternativas(self, *_):
            Elemento(self.pr, x=200, y=350, h=20, cena=self.cena, vai=self.aventura)
            Texto(self.p.oeste,"E aqui a aventura continua", foi=self.continua).vai()
            cena_fase = Cena("", vai=self.termina)
            self.cena.direita = cena_fase
        def aventura(self, *_):
            import age.aventura
        def continua(self, *_):
            import age.continua
        def termina(self, *_):
            import age.termina
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
    j = Jogo(style=dict(height="500px", width="650px"), did="_jogo_")
    
    class Aventura:
        def __init__(self):
            self.da = da = "_ativo/agentes/"
            i_c, self.i_p, i_p = "_cenas/cavernas.jpg", da+"pergaminho.png", da+"praia.jpeg"
            c = Mapa(i_c, conta_lado=4.3)
            self.c0, self.c1, self.c2 = c.salas[0], c.salas[1], c.salas[2]
            p = Mapa(i_p, conta_lado=4.3)
            self.p0, self.p1, self.p2 = p.salas[0], p.salas[1], p.salas[2]
            self.caverna()
    
        def caverna(self, *_):
            self.c0.norte.vai()
            diz = "No bilhete dizia que temos que encontrar o desenho de um homem"
            Texto(self.c0.norte, diz).vai()
            self.mapa = Elemento(self.i_p, x=60, y=218, h=60, w=50, o=0.3,
                                cena=self.c2.leste, vai=self.ve_mapa)
    
        def ve_mapa(self, *_):
            from jogos import Swap
            cena = self.c1.norte
            cena.vai()
            i_imagem = "_ativo/agentes/rupestre.jpg"
            t = Texto(cena, "Temos que encontrar umas aves próximas do mar", foi=self.aves)
            Swap(j, i_imagem, cena, 400, 400, 10, 10, 3, 3, venceu=t)
            m= self.mapa

        def aves(self):
            def anel(x=20, y=20, s=400, o=1):
                m.o, m.x, m.y, m.w, m.h = o, x, y, s, s
    
            i_a, i_s, i_g = self.da+"aves.png", self.da+"sinal.png", self.da+"graus.png"
            self.i_s, a, b = i_s, self.p1.leste, self.p1.sul
            self.p0.norte.vai()
            siga = "Siga as pegadas, você vai atintir a sua 'META'"
            pt = "Achamos uma parte do relógio de sol"
            m = Elemento(i_g, h=20, w=20, x=-1000, y=337, o=0.2, texto=pt, foi=anel, cena=b)
            Elemento(i_a, x=493, y=219, cena=a, texto=siga, foi=lambda:anel(512,337,20,0.2))
            self.sinal("PRAIA ➤➤➤", self.p1.norte, self.praia)
            self.sinal("SAMBA\nQUI➤➤", self.p1.oeste, self.sambaqui)
            self.sinal("CAVER\nNA➤➤", self.p2.norte, self.caverna)
            self.sinal("Templo ➤➤➤➤", self.p2.norte, self.caverna)
        def sinal(self, texto, cena, vai):
            pr = Elemento(self.i_s, x=10, y=319, cena=cena, vai=vai)
            style = "font-size: 1.5em; color: saddlebrown; margin:6px; pointer-events: none;"
            pr.elt.html = f'<h6 style="{style}">{texto}</h1>'
        def sambaqui(self, *_):
            self.p2.norte.vai()
            return
            from age.aventura import Aventura
            Aventura()
        def sambaqui(self, *_):
            self.p2.norte.vai()
            return
            from age.aventura import Aventura
            Aventura()
    
        def praia(self, *_):
            self.p2.norte.vai()
            return
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
    """Módulo age.continua"""
    from vitollino import Cena, Texto, Jogo, Elemento
    from cenario import Planilha, Mapa, Paisagens, Posiciona
    j = Jogo(style=dict(height="500px", width="650px"), did="_jogo_")
    
    class Continua:
        def __init__(self):
            self.da = da = "_ativo/agentes/"
            i_c, self.i_s, i_p = "_cenas/cavernas.jpg", da+"sinal.png", da+"praia.jpeg"
            p = Mapa(i_c, conta_lado=4.3)
            self.c0, self.c1, self.c2 = p.salas[0], p.salas[1], p.salas[2]
            p = Mapa(i_p, conta_lado=4.3)
            self.p0, self.p1, self.p2, self.grau = p.salas[0], p.salas[1], p.salas[2], None
            self.sinais()
            self.aves()
    
        def sinais(self):
            self.sinal("PRAIA ➤➤➤", self.p1.norte, self.praia)
            self.sinal("SAMBA\nQUI➤➤", self.p1.oeste, self.sambaqui)
            self.sinal("CAVER\nNA➤➤", self.p2.leste, self.caverna)
            self.sinal("PIRA\nTAS➤➤", self.p2.oeste, self.caverna)
            self.sinal("Templo\n➤➤", self.p0.sul, self.templo)
    
        def templo(self, *_):
            self.p1.oeste.vai()
    
        def caverna(self, *_):
            self.p0.norte.vai()
    
        def anel(self, x=20, y=20, s=400, o=1, vai=lambda *_: None):
            m= self.grau
            m.o, m.x, m.y, m.w, m.h = o, x, y, s, s
            vai()
    
        def aves(self):
            i_a, i_s, i_g = self.da+"aves.png", self.da+"sinal.png", self.da+"graus.png"
            self.i_s, a, b, a_a = i_s, self.p1.leste, self.p1.sul, self.anel
            self.p0.norte.vai()
            siga = "Siga as pegadas, você vai atingir a sua 'META'"
            pt = Texto(b, "Achamos uma parte do relógio de sol", foi=lambda:a_a(-4000)).vai
            self.grau = Elemento(i_g, h=20, w=20, x=-4000, y=337, o=0.2, vai=lambda *_: a_a(vai=pt), cena=b)
            Elemento(i_a, x=493, y=219, cena=a, texto=siga, foi=lambda:self.anel(512,337,20,0.2))
        def sinal(self, texto, cena, vai):
            pr = Elemento(self.i_s, x=10, y=319, cena=cena, vai=vai)
            style = "font-size: 1.5em; color: saddlebrown; margin:6px; pointer-events: none;"
            pr.elt.html = f'<h6 style="{style}">{texto}</h1>'
        def sambaqui(self, *_):
            self.p2.norte.vai()
            return
            from age.aventura import Aventura
            Aventura()
    
        def praia(self, *_):
            self.p2.norte.vai()
            return
            from age.aventura import Aventura
            Aventura()
    if __name__ == "__main__":
        Continua()         
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