import unittest
from unittest import TestCase

from _core.cenario import Planilha, Mapa
# from _core.vitollino import Cena, Inventario, INVENTARIO as INV


class TestPlanilha(TestCase):
    def setUp(self):
        self.planilha = Planilha("img", 4.3, )

    def test_criado(self, conta=4, lado=3):
        self.assertIsInstance(self.planilha, Planilha)
        self.assertEqual("img", self.planilha.imagem)
        self.assertEqual(lado, self.planilha.lado)
        self.assertEqual(conta, self.planilha.conta_lado)
        self.assertEqual(conta*lado, len(self.planilha.locais))
        # p100 = Planilha("img", 4.31)
        # self.assertEqual(31, p100.lado)

    def test_inicia(self):
        self.assertEqual(12, len(self.planilha._i))
        # self.fail()

    def test__img(self):
        self.assertIn("l0", self.planilha._img(0)["nome"])
        self.assertIn("img", self.planilha._img(0)["_im"])
        self.assertIn("0.00% 0.00%", self.planilha._img(0)["style"]['background-position'])
        self.assertIn('0.00% 33.33%', self.planilha._img(4)["style"]['background-position'])
        self.assertIn('75.00% 0.00%', self.planilha._img(3)["style"]['background-position'])

        # self.fail()


class TestMapa(TestPlanilha):
    def setUp(self):
        self.planilha = Mapa("img", 1.3)

    def test_criado(self, conta=4, lado=3):
        super(TestMapa, self).test_criado(conta=4)
        # self.assertFalse(self.planilha.salas)
        self.assertEqual(conta*lado, len(self.planilha.locais))
        # self.fail()

    def test_inicia(self):
        super(TestMapa, self).test_inicia()
        self.assertEqual(12, len(self.planilha._i))
        self.assertEqual(12, len(self.planilha.salas))
        self.assertIn("n", self.planilha.salas[0])
        # self.assertIn("nome", self.planilha.salas[0]["n"][1])
        # self.assertEqual("l0", self.planilha.salas[0]["n"][1]["nome"])
        self.assertEqual("l0", self.planilha.salas[0]["n"].nome)
        # self.assertIsInstance(self.planilha.s[0].norte, Cena)
        self.assertEqual("l0", self.planilha.s[0].norte.nome)

        # self.assertEqual([1], self.planilha.salas)

    def test__img(self):
        from vitollino import Cena, Sala, Portal, Inventario, INVENTARIO as INV
        q0 = self.planilha.n["s0"]
        self.assertIsInstance(q0, Sala)
        ln = s0 = q0.norte
        ll = q0.leste
        ls = q0.sul
        lo = q0.oeste
        s1 = q0.leste
        s1 = q0.oeste
        ln, ll, ls, lo = [Cena("img", nome=c) for c in "aeio"]
        self.assertEqual("l0", s0.nome)
        self.assertEqual("l3", s1.nome)
        self.assertEqual("s0", q0.nome)
        # self.assertEqual("s0",self.planilha._im["s0"])
        self.assertIsInstance(INV, Inventario)
        self.assertIsInstance(s0, Cena)
        self.assertIsInstance(s0.direita, Portal)

        # sl = Sala(n=ln, l=ll, s=ls, o=lo, nome="testar")
        sl = Sala(n=ln, l=ll, s=ls, o=lo, nome="testar")
        sc = sl.cenas
        def liga(og, ct, dt):
            # og.direita = dt
            ct.portal(direita=ct.portal(L=dt), esquerda=ct.portal(O=og))
            # dt.esquerda = og
        [liga(o, c, d) for o, c, d in zip(sc, sc[1:]+sc, sc[2:]+sc)]
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
    pass


if __name__ == "__main__":
    unittest.main()
