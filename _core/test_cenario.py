import unittest
from unittest import TestCase

from _core.cenario import Planilha, Mapa
from _core.vitollino import Cena


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
        s0 = self.planilha.n["s0"].norte
        s1 = self.planilha.n["s0"].leste
        self.assertEqual("l0", s0.nome)
        self.assertEqual(s1.direita.cena, s0.direita)

        # self.fail()
    pass


if __name__ == "__main__":
    unittest.main()
