<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# O Agente da SME - Cuidando dos Biomas
> E agora para algo totalmente diferente! <br>
> Aprenda Python resolvendo, modificando e criando jogos e desafios. <br>

Vamos criar uma ação para cuidar dos biomas na aba **[   caderno   ]**. 
Escolha na aba **[   guia   ]** uma opção de jogo.

<img src onerror="__did_got__('../../_prog/snct_ca.py')"></img>
<div id="_jogo_" style="position:relative; left:50px; min-height: 500px">
Aqui está um elemento identificado como '_jogo_'. 
Vai aparecer o seu jogo no espaço abaixo quando apertar o botão <b>[&nbsp;<i class="fa-solid fa-play"></i>&nbsp;]</b>.

</div>
<img id="caderno_cui" src onerror="__widget__(this.id)"></img>


```python
# pegue no guia algo para criar uma cena
from vitollino import Cena, Jogo, Elemento, Texto
j = Jogo(style=dict(height="450px", width="600px"), did="_jogo_") #.z()
a_cena = Cena("_cenas/amazonia1.jpg").vai()
fala = "Precisamos desarmar estas arapucas para preservar a fauna!!."
Elemento("_ativo/rosalinda.png", x=300, y=300, texto=fala, cena=a_cena)
```

#### LABASE
[footer](footer.md ':include')