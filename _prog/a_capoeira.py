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
v__.Elemento(img="_media/animais.png", y=90, x=300, w=200, h=200, cena=c__, tit="Tucano Tunoca", style={
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


