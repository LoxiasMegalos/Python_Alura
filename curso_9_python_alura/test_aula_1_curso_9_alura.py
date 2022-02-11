from unittest import TestCase
#from aula_1_curso_9_alura import Usuario, Lance, Leilao, Avaliador
from revisao_curso_9 import  Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def setUp(self):

        self.murillo = Usuario("Murillo")
        self.lance_murillo = Lance(self.murillo, 1000.0)
        self.leilao_carros = Leilao("Carros Velhos")

    # test_quando_adicionados_lances_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        '''
        murillo = Usuario("Murillo")
        yuri = Usuario("Yuri")

        lance_do_murillo = Lance(murillo, 1000.0)
        lance_do_yuri = Lance(yuri, 100.0)

        leilao = Leilao("Celular")
        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_murillo)


        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 1000.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
        '''

        thiago = Usuario("Thiago")
        lance_thiago = Lance(thiago, 999.0)

        self.leilao_carros.lances.append(lance_thiago)
        self.leilao_carros.lances.append(self.lance_murillo)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao_carros)

        menor_valor_esperado = 999.0
        maior_valor_esperado = 1000.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):

        thiago = Usuario("Thiago")
        lance_thiago = Lance(thiago, 999.0)

        self.leilao_carros.lances.append(self.lance_murillo)
        self.leilao_carros.lances.append(lance_thiago)


        avaliador = Avaliador()
        avaliador.avalia(self.leilao_carros)

        menor_valor_esperado = 999.0
        maior_valor_esperado = 1000.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):


        self.leilao_carros.lances.append(self.lance_murillo)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao_carros)

        self.assertEqual(1000, avaliador.menor_lance)
        self.assertEqual(1000, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        thiago = Usuario("Thiago")
        vini = Usuario("Vini")

        lance_thiago = Lance(thiago, 999.0)
        lance_vini = Lance(vini, 200)

        self.leilao_carros.lances.append(lance_vini)
        self.leilao_carros.lances.append(self.lance_murillo)

        self.leilao_carros.lances.append(lance_thiago)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao_carros)

        menor_valor_esperado = 200.0
        maior_valor_esperado = 1000.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
