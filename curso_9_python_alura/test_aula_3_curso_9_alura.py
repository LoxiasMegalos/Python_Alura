from unittest import TestCase
from aula_3_curso_9_alura import Usuario,Lances,Leilao #Avaliador2

class TestAvaliador2(TestCase):

    def setUp(self):
        self.murillo = Usuario("Murillo")
        self.lance_do_murillo = Lances(self.murillo, 600)
        self.leilao = Leilao("Carros")


    def test_deve_retornar_o_maior_e_menor_valor_quando_adiconados_em_ordem_crescente(self):

        thiago = Usuario("Thiago")
        luiz = Usuario("Luiz")

        lance_do_thiago = Lances(thiago, 950)
        lance_do_luiz = Lances(luiz, 800)

        self.leilao.propoe(lance_do_luiz)
        self.leilao.propoe(lance_do_thiago)
        self.leilao.propoe(self.lance_do_murillo)


        self.assertEqual(600, self.leilao.lance_menor)
        self.assertEqual(950, self.leilao.lance_maior)

    def test_deve_retornar_o_maior_e_menor_valor_quando_adiconados_em_ordem_decrescente(self):

        thiago = Usuario("Thiago")
        luiz = Usuario("Luiz")

        lance_do_thiago = Lances(thiago, 950)
        lance_do_luiz = Lances(luiz, 80)

        self.leilao.propoe(lance_do_luiz)
        self.leilao.propoe(lance_do_thiago)
        self.leilao.propoe(self.lance_do_murillo)


        self.assertEqual(80, self.leilao.lance_menor)
        self.assertEqual(950, self.leilao.lance_maior)

    def test_deve_retornar_o_mesmo_valor_tanto_maior_quanto_menor(self):


        self.leilao.propoe(self.lance_do_murillo)

        self.assertEqual(600, self.leilao.lance_menor)
        self.assertEqual(600, self.leilao.lance_maior)

    def test_deve_retornar_o_maior_e_o_menor_lance_quando_houver_mais_de_tres_lances_em_ordens_aleatorias(self):

        thiago = Usuario("Thiago")
        luiz = Usuario("Luiz")
        kayo = Usuario("Kayo")

        lance_do_thiago = Lances(thiago, 1200)
        lance_do_luiz = Lances(luiz, 12000)
        lance_do_kayo = Lances(kayo, 12)

        self.leilao.propoe(self.lance_do_murillo)
        self.leilao.propoe(lance_do_luiz)
        self.leilao.propoe(lance_do_kayo)
        self.leilao.propoe(lance_do_thiago)


        self.assertEqual(12, self.leilao.lance_menor)
        self.assertEqual(12000, self.leilao.lance_maior)