_SET0_ = {
    "script_name": "jo0", "script_div_id": "jo0",
    "height": 150, "title": "O Primeiro Jogo", "show_scenario": False, "console_height": 45
}  # _SEC_
from browser import document
from vitollino import Cena, STYLE
STYLE.update(height="500px")
jogo = document["_jogo_"]
jogo.html = ''
jogo.style.minHeight = "500px"
Cena("https://imgur.com/i0gCtpV.jpg", tela=jogo).vai()
#document["_so0_"].remove()
# _VIT_
# coloque sua cena aqui
from browser import document
from vitollino import Cena, STYLE
STYLE.update(height="500px")
jogo = document["_jogo_"]
jogo.html = ''
jogo.style.minHeight = "500px"
Cena("https://imgur.com/i0gCtpV.jpg", tela=jogo).vai()
