from unittest import TestCase
from curso_9_python_alura.aula_5_e_6_curso_9_alura import Leilao, Usuario, Lance
from curso_9_python_alura.excecoes import LanceInvalido

class TestLeilao(TestCase):

    def setUp(self):
        self.murillo = Usuario("Murillo", 500.0)
        self.lance_murillo = Lance(self.murillo, 100)
        self.leilao = Leilao("Carros")

    def test_nao_deve_permitir_propor_um_lance_em_odem_decrescente(self):

        with self.assertRaises(ValueError):
            thiago = Usuario("Thiago", 500.0)
            lance_thiago = Lance(thiago, 2001.0)

            self.leilao.propoe_lances(lance_thiago)
            self.leilao.propoe_lances(self.lance_murillo)


    # se o leilao nao tiver lances, deve permitir propor um lance

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):

        self.leilao.propoe_lances(self.lance_murillo)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    # se o ultimo usuario for diferente, deve permitir propor o lance

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):

        yuri = Usuario("Yuri", 500.0)
        lance_yuri = Lance(yuri,200)

        self.leilao.propoe_lances(self.lance_murillo)
        self.leilao.propoe_lances(lance_yuri)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    # se o ultimo usuario for o mesmo, não deve permitir propor um lance

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):

        lance_murillo200 = Lance(self.murillo, 200)
        '''
        try:
            self.leilao.adiciona_lances(self.lance_murillo)
            self.leilao.adiciona_lances(lance_murillo200)
            self.fail(msg="Não Lançou exceção")
        except ValueError:

            quantidade_de_lances_recebido = len(self.leilao.lances)
            self.assertEqual(1, quantidade_de_lances_recebido)
        '''
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe_lances(self.lance_murillo)
            self.leilao.propoe_lances(lance_murillo200)
