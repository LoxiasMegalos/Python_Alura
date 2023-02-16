#import sys
from excecoes import LanceInvalido
class Usuario:

    def __init__(self, nome, carteira):
        self.__usuario = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_e_valido(valor):
            raise LanceInvalido("Não pode propor um lance com um valor maior que o valor da carteira")
        else:
            lance = Lance(self.usuario, valor)
            leilao.propoe_lances(lance)
            self.__carteira -= valor

    @property
    def usuario(self):
        return self.__usuario

    @property
    def carteira(self):
        return self.__carteira

    def _valor_e_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, lance):
        self.nome = usuario
        self.valor = lance

class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maximo = 0.0
        self.minimo = 0.0

    @property
    def lances(self):
        return self.lances

    def propoe_lances(self, lance):
        if self._lance_e_valido(lance):
            if not self._tem_lances():
                self.minimo = lance.valor
            self.maximo = lance.valor
            self.__lances.append(lance)


    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        else:
            raise LanceInvalido("O Usuario nao pode dar 2 lances seguidos!")

    def _valor_maior_que_valor_anterior(self, lance):
        if lance.valor > self.lances[-1].valor:
            return True
        else:
            raise LanceInvalido("O valor do lance deve ser maior que o lance anterior")

    def _lance_e_valido(self, lance):
        return not self.__lances or (self._usuarios_diferentes(lance)
                                     and self._valor_maior_que_valor_anterior(lance))


