# Exercícios para Pensamento Computacional
# Open Source program Pynoplia - Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
# PDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
_SET0_ = {
    "script_name": "ca0", "script_div_id": "ca0",
    "height": 200, "title": "Macacos Encrenqueiros", "console_height": 180
}  # _SEC_
v__.Elemento(img="_media/indigena.png", y=90, x=50, w=200, h=200, cena=c__, tit="Curumim", style={
    "background-size": "300% 400%", "background-position": f"0% {100/3}%"})
v__.Elemento(img="_media/animais.png", y=90, x=250, w=200, h=200, cena=c__, tit="Macoca", style={
    "background-size": "200% 300%", "background-position": "0% 0%"})
v__.Elemento(img="_media/animais.png", y=90, x=450, w=200, h=200, cena=c__, tit="Camoca", style={
    "background-size": "200% 300%", "background-position": "0% 0%", "transform": "scaleX(-1)"})
# _VIT_
def macacos_encrenqueiros(macoca, camoca):
    """Observe os macacos e veja se é encrenca.
    """
    _ = macoca, camoca
    encrenca = macoca or camoca # faça seu cáculo e corrija esta linha
    return encrenca


assert macacos_encrenqueiros(True, True) is True
assert macacos_encrenqueiros(False, False) is True
assert macacos_encrenqueiros(False, True) is False

_SET1_ = {
    "script_name": "ca1", "script_div_id": "ca1",
    "height": 200, "title": "Tucano cantor", "console_height": 180
}  # _SEC_
v__.Elemento(img="_media/indigena.png", y=90, x=50, w=200, h=200, cena=c__, tit="Curumim", style={
    "background-size": "300% 400%", "background-position": f"0% {100/3}%"})
v__.Elemento(img="_media/animais.png", y=90, x=520, w=200, h=200, cena=c__, tit="Tucano Cantou", style={
    "background-size": "200% 300%", "background-position": "0% 100%"})
# _VIT_
def tucano_cantor(canta, hora):
    """Observe a hora que o tucano canta e veja se é encrenca.
    Lembre-se que o tucano só deve cantar entre 7 e 20 horas.
    """

    encrenca = canta or hora # faça seu cáculo e corrija esta linha
    return encrenca


assert tucano_cantor(True, 9) is False
assert tucano_cantor(False, 21) is False
assert tucano_cantor(True, 6) is True

_SET2_ = {
    "script_name": "ca2", "script_div_id": "ca2",
    "height": 200, "title": "Cocar de Tucanos", "console_height": 180
}  # _SEC_
v__.Elemento(img="_media/indigena.png", y=90, x=50, w=200, h=200, cena=c__, tit="Curumim", style={
    "background-size": "300% 400%", "background-position": f"0% {100/3}%"})
v__.Elemento(img="_media/animais.png", y=90, x=520, w=200, h=200, cena=c__, tit="Tucano Cantou", style={
    "background-size": "200% 300%", "background-position": "0% 100%"})

# _VIT_
def fazendo_cocar(um_bando, outro_bando):
    """Retorna se a contagem dos bandos ou a soma é sete.
    """
    resultado = um_bando - outro_bando
    return resultado


assert fazendo_cocar(7, 4) is True
assert fazendo_cocar(3, 4) is True
assert fazendo_cocar(2, 4) is False

_SET3_ = {
    "script_name": "ca3", "script_div_id": "ca3",
    "height": 200, "title": "Bando de Araras", "console_height": 180
}  # _SEC_
v__.Elemento(img="_media/indigena.png", y=90, x=50, w=200, h=200, cena=c__, tit="Curumim", style={
    "background-size": "300% 400%", "background-position": f"0% {100/3}%"})
v__.Elemento(img="https://imgur.com/SYOroZK.png", y=-40, x=260, w=400, h=180, cena=c__, tit="Bando de Araras")
# _VIT_
def contando_araras(um_bando):
    """Retorna verdadeiro se a contagem do bando é em torno de vinte.
    """
    resultado = um_bando
    return resultado


assert contando_araras(22) is True
assert contando_araras(19) is True
assert contando_araras(25) is False
assert contando_araras(17) is False

_SET4_ = {
    "script_name": "ca4", "script_div_id": "ca4",
    "height": 200, "title": "Elogiando Amigos", "console_height": 180
}  # _SEC_


from vitollino import Jogo
def animal(xpos, nome, bpos):
    return v__.Elemento(img="_media/animais.png", y=90, x=130 + 130 * xpos, w=200, h=200, cena=c__, tit=nome, style={
        "background-size": "200% 300%", "background-position": f"{bpos[0]}% {bpos[1]}%"})


v__.Elemento(img="_media/indigena.png", y=90, x=0, w=200, h=200, cena=c__, tit="Curumim Sagaz", style={
    "background-size": "300% 400%", "background-position": f"0% {100/3}%"})
Jogo.ANIMAIS = [animal(x, n, b) for x, (n, b) in enumerate(
    [("mico", (0, 0)), ("tucano", (0, 100)), ("coruja", (0, 50)), ("tatu", (100, 0))]
)]
# _VIT_
from vitollino import Jogo
def elogia_os_amigos():
    """Use a coleção de animais e para cada animal use a propriedade tit para trabalhar com o nome.
    """
    animais = Jogo.ANIMAIS
    for _ in __:  # conserte esta linha
        nome = animal.tit
        animal.tit = "conserte esta linha também"
elogia_os_amigos()
assert Jogo.ANIMAIS[0].tit == "mico sagaz"
assert Jogo.ANIMAIS[1].tit == "tucano sagaz"
assert Jogo.ANIMAIS[2].tit == "coruja sagaz"
assert Jogo.ANIMAIS[3].tit == "tatu sagaz"
_SET5_ = {
    "script_name": "ca5", "script_div_id": "ca5",
    "height": 200, "title": "Resfriado", "console_height": 180
}  # _SEC_
v__.Elemento(img="_media/indigena.png", y=90, x=50, w=200, h=200, cena=c__, tit="Curumim", style={
    "background-size": "300% 400%", "background-position": f"0% {100/3}%"})
# _VIT_
def resfriado(a_fazer):
    """Em construção.
    """
    resultado = a_fazer
    return resultado

_SET6_ = {
    "script_name": "ca6", "script_div_id": "ca6",
    "height": 200, "title": "Zoado", "console_height": 180
}  # _SEC_
v__.Elemento(img="_media/indigena.png", y=90, x=50, w=200, h=200, cena=c__, tit="Curumim", style={
    "background-size": "300% 400%", "background-position": f"0% {100/3}%"})
# _VIT_
def zoado(a_fazer):
    """Em construção.
    """
    resultado = a_fazer
    return resultado

_SET7_ = {
    "script_name": "ca7", "script_div_id": "ca7",
    "height": 200, "title": "Zombeteira", "console_height": 180
}  # _SEC_
v__.Elemento(img="_media/indigena.png", y=90, x=50, w=200, h=200, cena=c__, tit="Curumim", style={
    "background-size": "300% 400%", "background-position": f"0% {100/3}%"})
# _VIT_
def zombeteira(a_fazer):
    """Em construção.
    """
    resultado = a_fazer
    return resultado


