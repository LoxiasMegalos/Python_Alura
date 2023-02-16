import sys

class Usuario:

    def __init__(self, nome, carteira):
        self.__usuario = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if (valor > self.carteira):
            #self.__carteira += 0
            raise ValueError("Não pode propor um lance com um valor maior que o valor da carteira")
        else:
            lance = Lances(self.usuario, valor)
            leilao.adiciona_lances(lance)
            self.__carteira -= valor


    @property
    def usuario(self):
        return self.__usuario

    @property
    def carteira(self):
        return self.__carteira

class Lances:

    def __init__(self, usuario, lance):
        self.nome = usuario
        self.valor = lance


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maximo = sys.float_info.min
        self.minimo = sys.float_info.max

    @property
    def lances(self):
        return self.__lances

    def adiciona_lances(self, lance):
        if not self.__lances or self.__lances[-1].nome != lance.nome and lance.valor > self.__lances[-1].valor:
            if lance.valor > self.maximo:
                self.maximo = lance.valor
            if lance.valor < self.minimo:
                self.minimo = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError("ERRO AO PROPOR LANCE")



    def informa_maior_e_menor(self):
        return "Leilão {} - maior lance: {} | menor lance: {}".format(self.descricao, self.maximo, self.minimo)

class Avalia:

    def __init__(self):
        self.maximo = sys.float_info.min
        self.minimo = sys.float_info.max

    def avalia(self, leilao:"espera que seja passado um Leilao"):
        for lance in leilao.lances:
            if lance.valor > self.maximo:
                self.maximo = lance.valor
            if lance.valor < self.minimo:
                self.minimo = lance.valor


'''
murillo = Usuario("Murillo")
thiago = Usuario("Thiago")
lance_murillo = Lances(murillo, 100.0)
lance_thiago = Lances(thiago, 2001.0)
leilao = Leilao("Carros")
leilao.adiciona_lances(lance_murillo)
leilao.adiciona_lances(lance_thiago)
leilao.avalia()
print(leilao.informa_maior_e_menor())
'''

