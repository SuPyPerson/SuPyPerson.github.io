_SET0_ = {
    "script_name": "al0", "script_div_id": "al0",
    "height": 150, "title": "Aldeia Queimada"
}  # _SEC_
v__.Elemento(img="_media/aldeia_queimada.jpg", y=100, x=50, w=300, h=200, cena=c__)
# _VIT_
cordel = """Quando o índio percebe
Deus! Já é tarde demais...
Os que se diziam amigos
Eram inimigos fatais.
Tomariam suas terras
Com covardia voraz."""
print(cordel)
_SET1_ = {
    "script_name": "al1", "script_div_id": "al1",
    "height": 150, "title": "A linguagem Python"
}  # _SEC_
v__.Elemento(img="_media/vaso_boitata.png", y=90, x=250, w=150, h=200, cena=c__, tit="O Vaso do Boitatá")
# _VIT_
vaso = "Vaso do Boitata"
python_tem_tipo = True
print(type(vaso))
print(type(python_tem_tipo))
# remova o '#' e veja um erro de mistura de tipo
#print(type(vaso + python_tem_tipo))
_SET2_ = {
    "script_name": "al2", "script_div_id": "al2",
    "height": 170, "title": "A Sintaxe Python"
}  # _SEC_
v__.Elemento(img="_media/animais.png", y=90, x=10, w=200, h=200, cena=c__, tit="Mico Coim", style={
    "background-size": "200% 300%", "background-position": "0% 0%"})
v__.Elemento(img="_media/animais.png", y=90, x=180, w=200, h=200, cena=c__, tit="Tatu Utat", style={
    "background-size": "200% 300%", "background-position": "100% 0%"})
v__.Elemento(img="_media/animais.png", y=90, x=360, w=200, h=200, cena=c__, tit="Coruja Jacrou", style={
    "background-size": "200% 300%", "background-position": "0% 50%"})
v__.Elemento(img="_media/animais.png", y=90, x=520, w=200, h=200, cena=c__, tit="Tucano Cantou", style={
    "background-size": "200% 300%", "background-position": "0% 100%"})
# _VIT_
o_mico = "Coim"
o_tatu = "Utat"
tatu = "Tatu "
a_coruja, o_tucano = "Jacrou", "Cantou"
print("O mico ",o_mico, "e o tatu", o_tatu)
# pode juntar dois textos usando o símbolo "+"
print(tatu + o_tatu)
print("A coruja", a_coruja, "e o tucano", o_tucano)
# o pajé quiz confundir os caraíbas e trocou o nome dos bichos
a_coruja, o_tucano = o_tucano, a_coruja
print("A coruja", a_coruja, "e o tucano", o_tucano)
_SET3_ = {
    "script_name": "al3", "script_div_id": "al3",
    "height": 170, "title": "Números e Operações"
}  # _SEC_
def st(x, y):
    return {"background-size": "200% 300%", "background-position": f"{x*100}% {y*50}%"}
def an(x, y, l, c, n="Mico"):
    return v__.Elemento(img="_media/animais.png", y=y, x=x, w=60, h=60, cena=c__, tit=n, style=st(l, c))
mi, ta, co, tu = (lambda x, y,: an(x, y, 0, 0, "mico"), lambda x, y,: an(x, y, 1, 0, "tatu"),
                  lambda x, y,: an(x, y, 0, 1, "coruja"), lambda x, y,: an(x, y, 0, 2, "tucano"))
[mi(10+60*px, 90) for px in range(3)]
[ta(190+60*px, 90) for px in range(6)]
[co(10+60*px, 140) for px in range(5)]
[tu(310+60*px, 140) for px in range(4)]
[mi(10+60*px, 190) for px in range(7)]
[ta(10+60*7+60*px, 190) for px in range(2)]
[co(10+60*px, 240) for px in range(6)]
[tu(10+60*6+60*px, 240) for px in range(3)]
# _VIT_
# Corrija todos os nomes e valores para que fique certo
conta_micos, conta_tatus, conta_corujas, conta_tucanos = 0+0, 0+0, 0+0, 0+0
conta_mamíferos, conta_aves = conta_micos+ conta_micos, conta_tatus+conta_tatus
conta_animais = 1*1
proporção_aves = conta_micos *100/conta_animais
proporção_mamíferos = conta_micos *100/conta_animais
print("conta mamíferos: ", conta_aves, "conta aves: ", conta_aves)
print("conta micos: ", conta_aves, "conta tatus: ", conta_aves)
print("conta corujas: ", conta_aves, "conta tucanos: ", conta_aves)
print("animais: ", conta_aves, f"proporção de aves: {conta_aves}%", f"proporção de mamíferos: {conta_aves}%")
_SET4_ = {
    "script_name": "al4", "script_div_id": "al4",
    "height": 150, "title": "Caminha na Estrada"
}  # _SEC_
from kwarwp.kwarapp import main as kwarwp_main, Indio
from vitollino import Jogo, STYLE
MAPA = """
||||||
p....&
||||||
"""
Jogo.Kaiowa = Indio
Jogo.kwarwp = lambda ind: kwarwp_main(vitollino=Jogo, medidas=STYLE, mapa=MAPA, indios=(ind,), tela=c__.tela)
# _VIT_
from vitollino import Jogo as Povo
class Curumim(Povo.Kaiowa):
    def executa(self):
        self.direita()
        self.anda()
        self.anda()
        self.fala("oi")

Povo.kwarwp(Curumim).executa()
