import pytest
from curso_9_python_alura.aula_5_e_6_curso_9_alura import Usuario, Lance, Leilao

@pytest.fixture()
def murillo():
    return Usuario("Murillo", 1000.0)

@pytest.fixture()
def leilao():
    return Leilao("Carros")

def test_deve_subtrair_o_valor_da_carteira_do_usuario_quando_este_propor_um_lance(murillo, leilao):

    #murillo = Usuario("Murillo", 100)
    #leilao = Leilao("Carros")
    murillo.propoe_lance(leilao,50.0)
    assert murillo.carteira == 950.0

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_valor_da_carteira(murillo, leilao):

    #vini = Usuario("Vini", 100.0)
    #leilao = Leilao("Celular")
    murillo.propoe_lance(leilao, 1.0)
    assert murillo.carteira == 999.0

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(murillo, leilao):

    #vini = Usuario("Vini",100.0)
    #leilao = Leilao("Celular")
    murillo.propoe_lance(leilao, 1000.0)
    assert murillo.carteira == 0

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(murillo, leilao):

    with pytest.raises(ValueError):
        #vini = Usuario("vini", 100.0)
        #leilao = Leilao("avioes")
        murillo.propoe_lance(leilao, 2090)