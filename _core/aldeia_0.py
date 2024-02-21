_SET0_ = {
    "script_name": "al0", "script_div_id": "al0",
    "height": 150, "title": "Aldeia Queimada"
}  # _SEC_
v__.Elemento(img="_media/queimada.jpg", y=100, x=50, w=300, h=200, cena=c__)
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
