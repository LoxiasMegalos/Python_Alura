import pytest

from curso_9_python_alura.aula_4_curso_9_alura import Usuario, Leilao

#um usuario so pode dar um lance que pode ser até o valor da carteira
#nunca maior que oq ele tem
#Subtrair o valor quando ele dar o lance
@pytest.fixture()
def vini():
    return Usuario("vini",100.0)

@pytest.fixture()
def leilao():
    return Leilao("Celular")

def test_deve_subtrair_o_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):

    #murillo = Usuario("Murillo", 100)
    #leilao = Leilao("Carros")
    vini.propoe_lance(leilao,50.0)
    assert vini.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_valor_da_carteira(vini, leilao):

    #vini = Usuario("Vini", 100.0)
    #leilao = Leilao("Celular")
    vini.propoe_lance(leilao, 1.0)
    assert vini.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(vini, leilao):

    #vini = Usuario("Vini",100.0)
    #leilao = Leilao("Celular")
    vini.propoe_lance(leilao, 100.0)
    assert vini.carteira == 0

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(vini, leilao):

    with pytest.raises(ValueError):
        #vini = Usuario("vini", 100.0)
        #leilao = Leilao("avioes")
        vini.propoe_lance(leilao, 200)
