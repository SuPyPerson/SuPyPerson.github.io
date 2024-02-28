_SET0_ = {
    "script_name": "so0", "script_div_id": "so0",
    "height": 150, "title": "Aldeia Queimada"
}  # _SEC_
from browser import document
document["_so0_"].remove()
# _VIT_
from browser import document, html
base = document["_sonho_"]
base.html = ""
texto = html.P("O Sonho de Curumim",Class="title")
corpo = html.DIV(texto, Class="hero-body")
hero = html.DIV(corpo, Class="hero is-primary")
_ = base <= hero
_SET1_ = {
    "script_name": "so1", "script_div_id": "so1",
    "height": 150, "title": "Aldeia Queimada"
}  # _SEC_
from browser import document
document["_so1_"].remove()
# _VIT_
from browser import document, html
base = document["_sonho_"]
base.html = ""
imagem = html.IMG(src="https://bulma.io/images/placeholders/1280x960.png", alt="Placeholder image")
figura = html.FIGURE(imagem,Class="image is-4by3")
card_img = html.DIV(figura,Class="card-image")
texto = html.DIV(html.P("Lorem ipsum dolor sit amet"), Class="content")
media = html.DIV(Class="media")
card_cnt = html.DIV((media, texto),Class="card-content")
card = html.DIV((card_img, card_cnt),Class="card")
horror = html.SPAN("horror",Class="tag")
indie = html.SPAN("indie",Class="tag")
tags = html.DIV((indie, horror), Class="tags are-medium")
_ = base <= card
_ = base <= tags
