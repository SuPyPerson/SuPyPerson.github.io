<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# Agentes da ESCOLA
> E, de repente, o rádio tocou</br>
> Cena de cinema </br>

+ Central dos Agentes +
  
    Os Agentes da ESCOLA são chamados para investigar o cuidado com animais.
  
    Vamos aprender a usar uma planilha com imagens. Aqui podemos criar caminhos alternativos
    para nossa história.
  
    ```python
    """Módulo pet.main"""
    from vitollino import Cena, Texto, Jogo, Elemento
    from cenario import Planilha, Paisagens
    Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
  
    class Inicia:
        def __init__(self):
            i_praia, self.pr = "_ativo/agentes/praia.jpeg", "_ativo/agentes/pergaminho.png"
            mapa_praia = Planilha(i_praia, conta_lado=4.3)
            self.p = p = Paisagens(mapa_praia.j)
            p.norte.vai()
            self.alternativas()
            self.mapa.o, self.cena = 0.2 , p.norte
        def alternativas(self, *_):
            Elemento(self.pr, x=200, y=350, h=20, cena=self.cena, vai=self.aventura)
            Texto(self.cena,"E aqui a aventura continua", vai=self.continua)
            self.cena.direita.vai = self.termina
        def aventura(self):
            import pet.aventura
        def continua(self):
            import pet.continua
        def termina(self):
            import pet.termina
    if __name__ == "__main__":
        Inicia()
    ```
<button class="btn btn-primary" onclick="__copy_clip__(this)">Copia o código</button>


#### LABASE
[footer](footer.md ':include')