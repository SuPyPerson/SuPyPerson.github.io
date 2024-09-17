import unittest
from unittest import TestCase, mock
from unittest.mock import MagicMock

from cenario import Planilha, Mapa, Paisagens, Paisagem, Typer
import _core.vitollino as vit


from vitollino import Cena, Inventario, Sala, Portal, INVENTARIO as INV


class TestPlanilha(TestCase):
    def setUp(self):
        self.planilha = Planilha("img", 4.3, )

    def test_criado(self, conta=4, lado=3):
        self.assertIsInstance(self.planilha, Planilha)
        self.assertEqual("img", self.planilha.imagem)
        self.assertEqual(lado, self.planilha.lado)
        self.assertEqual(conta, self.planilha.conta_lado)
        self.assertEqual(conta * lado, len(self.planilha.locais))
        # p100 = Planilha("img", 4.31)
        # self.assertEqual(31, p100.lado)

    def test_inicia(self):
        self.assertEqual(12, len(self.planilha.i))
        # self.fail()

    def test__img(self):
        # self.assertIn("l0", self.planilha._img(0)["nome"])
        # self.assertIn("img", self.planilha._img(0)["_im"])
        self.assertIn("0.00% 0.00%", self.planilha._img(0)['background-position'])
        # self.assertIn('0.00% 33.33%', self.planilha._img(4)['background-position'])
        self.assertIn('0.00% 50.00%', self.planilha._img(4)['background-position'])
        # self.assertIn('75.00% 0.00%', self.planilha._img(3)['background-position'])
        self.assertIn('100.00% 0.00%', self.planilha._img(3)['background-position'])

        # self.fail()


class TestMapa(TestPlanilha):

    def setUp(self):
        self.portal = MagicMock(name='portal')
        def fake_portal(itself, esquerda=None, direita=None, meio=None, **kwargs):
            itself._meio = meio
            # print("fake portal", kwargs, esquerda, meio, direita) if "N" in kwargs else None
            return self.portal

        with mock.patch.object(Cena, "portal", fake_portal):
            self.p0 = Paisagens("abcd", 4, nome="As_Paisagens0")
            self.p1 = Paisagens("efgh", 4, nome="As_Paisagens1")
            self.planilha = Mapa([[self.p0], [self.p1]], 4.2)

    def test_criado(self, conta=1, lado=2):
        # super(TestMapa, self).test_criado(conta=4)
        # self.assertFalse(self.planilha.salas)
        self.assertEqual(conta * lado, len(self.planilha.locais))
        # self.fail()

    def test_inicia(self):
        # self.assertEqual(4, len(list(self.planilha.img)))
        # self.assertEqual("4", list(self.planilha.img))
        n_salas = 2
        # super(TestMapa, self).test_inicia()
        # self.assertEqual(n_salas, len(self.planilha._i))
        self.assertEqual(n_salas, len(self.planilha.nome_salas))
        self.assertEqual(n_salas, len(self.planilha.salas))
        self.assertEqual(n_salas+2, len(self.planilha.imagem))
        self.assertEqual(1, len(self.planilha.imagem[1]))
        self.assertIn("n", self.planilha.salas[0][0].__dict__)
        # self.assertIn("nome", self.planilha.salas[0]["n"][1])
        # self.assertEqual("l0", self.planilha.salas[0]["n"][1]["nome"])
        self.assertEqual("As_Paisagens0", self.planilha.salas[0][0].nome)
        # self.assertIsInstance(self.planilha.s[0].norte, Cena)
        self.assertEqual("As_Paisagens0.n", self.planilha.salas[0][0].norte.nome)

        # self.assertEqual([1], self.planilha.salas)
    def test__img(self):
        port = MagicMock
        c0 = self.planilha.local["As_Paisagens0.n"]
        self.assertIsInstance(c0, Paisagem)
        q0 = self.planilha.sala["As_Paisagens0"]
        # self.assertIn("AS", self.planilha.sala, self.planilha.sala)
        q1 = self.planilha.sala["As_Paisagens1"]
        self.assertIsInstance(q0, Paisagens)
        ln = s0 = q1.norte
        ll = q0.leste
        ls = q0.sul
        lo = q0.oeste
        s1 = q0.leste
        ln, ll, ls, lo = [Paisagem("img", nome=c) for c in "aeio"]
        self.assertEqual("As_Paisagens1.n", s0.nome)
        self.assertEqual("As_Paisagens0.l", s1.nome)
        self.assertEqual("As_Paisagens0", q0.nome)
        # self.assertEqual("s0",self.planilha._im["s0"])
        self.assertIsInstance(INV, Inventario)
        self.assertIsInstance(s0, Paisagem)
        self.assertIsInstance(s0.direita, port)
        self.assertIsInstance(s0.meio, port)
        self.assertIsInstance(q1.norte.meio, port)
        '''
        self.assertIsInstance(q1.norte.meio.portal, Portal)
        self.assertNotIsInstance(s0.meio.portal, Portal)

        # sl = Sala(n=ln, l=ll, s=ls, o=lo, nome="testar")
        sl = Sala(n=ln, l=ll, s=ls, o=lo, nome="testar")
        sc = sl.cenas

        def liga(og, ct, dt):
            # og.direita = dt
            ct.portal(direita=ct.portal(L=dt), esquerda=ct.portal(O=og))
            # dt.esquerda = og

        [liga(o, c, d) for o, c, d in zip(sc, sc[1:] + sc, sc[2:] + sc)]
        self.assertEqual("a", sl.norte.nome)
        self.assertEqual("e", sl.leste.nome)
        self.assertEqual("i", sl.sul.nome)
        self.assertEqual("o", sl.oeste.nome)
        self.assertEqual("e", sl.norte.direita.portal.destino.nome)
        self.assertEqual("e", sl.norte.esquerda.portal.destino.nome)
        self.assertEqual("i", sl.leste.direita.portal.destino.nome)
        self.assertEqual("a", sl.leste.esquerda.portal.destino.nome)
        self.assertEqual("e", sl.sul.esquerda.portal.destino.nome)
        self.assertEqual("i", sl.oeste.esquerda.portal.destino.nome)
        # s0.direita = s1
        self.assertIsInstance(s0.direita.portal.destino, Cena)
        # self.assertIsInstance(sl.norte.direita.portal, Cena)
        # s0.direita.portal.do_vai()
        # s1.vai()
        # s0.direita.vai()
        # s0.vai_direita()
        self.assertEqual('', [al.esquerda.portal for al in [ln, ll, ls, lo]])
        # self.assertEqual('', [al.direita.portal.destino.nome for al in [ln]])
        s0.vai_esquerda()
        self.assertEqual("l3", INV.cena.nome)
        s1.vai_esquerda()
        self.assertEqual("l3", INV.cena.nome)
        self.assertEqual(s1, INV.cena)

        # self.fail()
        '''

    pass


if __name__ == "__main__":
    unittest.main()


class TestPaisagens(TestCase):
    def setUp(self):
        self.paisagens = Paisagens("abcd", 4, nome="As_Paisagens")

    def test_criado(self, conta=4, lado=3):
        self.assertIsInstance(self.paisagens, Paisagens)
        self.assertEqual("As_Paisagens", self.paisagens.nome)
        self.assertIsInstance(self.paisagens.n, Paisagem)
        self.assertEqual("a", self.paisagens.n.img)
        self.assertIsInstance(self.paisagens.l, Paisagem)
        self.assertEqual("b", self.paisagens.n.img)
        self.assertEqual(self.paisagens.o, self.paisagens.n.direita.portal.destino)
        self.assertIsInstance(self.paisagens.n.direita.portal.destino, Paisagem)

        # p100 = Planilha("img", 4.31)
        # self.assertEqual(31, p100.lado)


class TestTyper(TestCase):
    def setUp(self):
        self.typer = Typer("abcd")
        self.p0 = Paisagens("abcd", 4, nome="As_Paisagens")

        class NewTyper(Typer):
            def str(self):
                return self.ref.upper()

            def paisagens(self):
                return self.ref
        self.typer = Typer("abcd")
        self.new_typer = NewTyper("abcd")
        self.pss_typer = NewTyper(self.p0)

    def test_criado(self, conta=4, lado=3):
        self.assertIsInstance(self.new_typer, Typer)
        self.assertEqual("abcd", self.typer("abcd"))
        self.assertEqual("ABCD", self.new_typer.str())
        self.assertEqual("abcd", self.new_typer.ref)
        # self.assertEqual("abcd", self.new_typer("abcd"))
        self.assertEqual("ABCD", self.new_typer("abcd"))
        self.assertEqual(self.p0, self.pss_typer(self.p0))

