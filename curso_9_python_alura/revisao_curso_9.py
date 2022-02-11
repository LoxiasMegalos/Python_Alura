import sys

class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class Lance:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances


class Avaliador:

    def __init__(self):
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def avalia(self, leilao : "espera receber um leilao"):

        for lance in leilao.lances:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance .valor

murillo = Usuario("Murillo")
thiago = Usuario("Thiago")
lance_thiago = Lance(thiago, 999.0)
lance_murillo = Lance(murillo, 1000.0)
leilao_carros = Leilao("Carros Velhos")
leilao_carros.lances.append(lance_murillo)
leilao_carros.lances.append(lance_thiago)

for lance in leilao_carros.lances:
    print("{} | {}".format(lance.nome.nome, lance.valor))

resultado = Avaliador()
resultado.avalia(leilao_carros)

print("O maior lance no leilão: {} foi de {}  e o menor foi de {}".format(leilao_carros.descricao, resultado.maior_lance, resultado.menor_lance))


