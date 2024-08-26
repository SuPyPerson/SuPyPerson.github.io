# Vitollino - Módulo para Jogos

Vitollino é um engenho para construção de jogos inteligentes para ensino de programação ou qualquer outro asunto que possa ser ensinado por games.

Este ambiente facilita a aprendizagem da linguagem Python. O jogo é dirigido principalmente ao ensino de programação de computadores para jovens e crianças do ensino médio e fundamental.

O engenho Vitollino é programado em Brython.

# Jogo

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


# Cena
Cria uma cena do jogo.
```python
cena = Cena(japones).vai()
japones, relogio = local.format("japones"), local.format("relogio")
"No início da linha *japones* e *relogio* sã apelidos que criamos"
"japones aqui diz que a imagem da cena á aquela da figura japones.jpg"
Texto(cena, "Olá, Vamos construir o Jardim Radical!").vai()
"No texto, o apelido *cena* diz a cena que vai mostrar o texto que é colocado após a vírgula"
```

# Sala
Cria uma sala com quatro cenas
  ```python
  cenas = "japones relogio mirante tomjobim".split()
  "Vamos usar a sala do exemplo anterior"
  jardim = Sala(*[f"/_ativo/jardim/{cena}.jpg" for cena in cenas])
  cena = jardim.sul.vai()
  "Escolhemos a cena sul, o mirante, para ser a cena inicial"
  ```
# Labirinto
Junta cinco salas em um formato de cruz.
  ```python
  cenas = "japones relogio mirante tomjobim".split()
  "Vamos usar a sala do exemplo anterior"
  jardim = Sala(*[f"/_ativo/jardim/{cena}.jpg" for cena in cenas])
  cena = jardim.sul.vai()
  "Escolhemos a cena sul, o mirante, para ser a cena inicial"
  ```
