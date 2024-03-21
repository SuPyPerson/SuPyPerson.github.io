<!---
Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
-->
# O Primeiro Jogo
> Vou dizer minha mulher, Paraná </br>
> Capoeira me venceu, Paraná </br>
> Paraná ê, Paraná ê, Paraná

<img src onerror="__did_got__('../../_prog/a_capoeira.py')"></img>

+ Macacos Encrenqueiros +
 
  <img id="ca0" src onerror="__widget__(this.id)"/>
 
    Enquanto andava no mato, Curumim descobre dois macacos surtados, Macoca e Camaco.
    Se os dois te virem eles te atacam. Eles também vão te atacar se nenhum deles te ver.
    Se somente um te ver não vai ter problema. Escreva uma função *macacos_encrenqueiros*
    para saber se vai ter encrenca. A função recebe dois argumentos *macoca* e *camoca*
    O argumento *macoca* é *True* se macoca está te vendo. O mesmo valhe para *camoca*
    
    ```python
    """A partir da lógica booleana, uma condição pode ser verdadeira ou falsa"""
    verdadeiro = True or True
    tambem_verdadeiro = True and True
    verdadeiro_ainda = True or False
    falso = True and False
    tambem_falso = False or False
    falso_ainda = False and False
    ```
    Você pode aprender um pouco de lógica olhando as expressões acima.
    Também pode combinar os termos e fazer algo mais sofisticado.
    ```python
    """A partir da lógica booleana, uma condição pode ser verdadeira ou falsa"""
    verdadeiro = (True or True) or (True and True)
    tambem_verdadeiro = (True and True) and (True or False)
    verdadeiro_ainda = (True and True) or (True or False)
    falso = (True and False) or (False and True)
    tambem_falso = (True or False) and (False and True)
    falso_ainda = (False and False) or (False and True)
   ```

+ Tucano Cantor +
 
  <img id="ca1" src onerror="__widget__(this.id)"/>
 
    Enquanto andava no mato, Curumim encontra o tucano Cantou.
    Para que Curumim possa dormir em paz, Cantou só deve cantar entre 7 e 20 horas.
    Escreva uma função *tucano_cantor* para saber se vai ter encrenca.
    A função recebe dois argumentos *canta* e *hora*
    O argumento *canta* é *True* se o tucano está cantando. A *hora* diz a hora que ele cantou.
    
    ```python
    """você pode comparar dois números e retornar True ou False"""
    verdadeiro = 10 > 5
    tambem_verdadeiro = 4 < 10
    verdadeiro_ainda = 10 <= 10
    falso = 5 > 10
    tambem_falso = 11 <= 10
    falso_ainda = not (5 > 4)
    ```
    Você pode aprender um pouco de comparações olhando as expressões acima.
    Também pode combinar os termos e fazer algo mais sofisticado.
    ```python
    """A partir da lógica booleana, uma condição pode ser verdadeira ou falsa"""
    verdadeiro = (5 > 4) or (5 > 5)
    tambem_verdadeiro = (4 < 5) and (5 >= 5)
    verdadeiro_ainda = 5 < 8 < 10
    falso = (8 > 9) or (6 < 4)
    tambem_falso = 5 < 10 < 7
    falso_ainda = 9 > 3 > 5
   ```
  
+ Cocar de Tucanos +
 
  <img id="ca2" src onerror="__widget__(this.id)"/>
 
    Curumim está fazendo um cocar. Para isso ele vai roubar uma pena de cada tucano que encontrar.
    O cocar precisa ter sete penas. Ele vai e avista dois bandos de tucanos.
    Ele vai poder fazer o cocar se a soma dos dois bandos der sete, ou se somente um bando já tiver sete.
    Escreva uma função *fazendo_cocar* para saber se Curumim vai ter sucesso.
    A função recebe dois argumentos *um_bando* e *outro_bando*
    O argumento *um_bando* é a contagem de tucanos no bando. O argumento *outro_bando* também.
    
    ```python
    """você pode comparar dois números e retornar True ou False"""
    verdadeiro = 3+3 > 5
    tambem_verdadeiro = 4 < 5+5
    verdadeiro_ainda = 3+7 == 4+6 #(== é a comparação igual)
    falso = 2+2 > 10-5
    tambem_falso = 3-1 <= 5+4 <= 7
    falso_ainda = not (4+4 > 12-6)
    ```

#### LABASE
[footer](footer.md ':include')