
import sys

class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lances:

    def __init__(self, usuario, lance):
        self.usuario = usuario
        self.valor = lance

class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.lance_maior = sys.float_info.min
        self.lance_menor = sys.float_info.max

    def propoe(self, lance: "Lance da classe Lances"):
        if (lance.valor > self.lance_maior):
            self.lance_maior = lance.valor
        if (lance.valor < self.lance_menor):
            self.lance_menor = lance.valor
        self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]


class Avaliador2:

    def __init__(self):
        self.lance_maior = sys.float_info.min
        self.lance_menor = sys.float_info.max

    def avalia(self, leilao : "espera que seja um leilao"):
        for lance in leilao.lances:
            if(lance.valor > self.lance_maior):
                self.lance_maior = lance.valor
            if(lance.valor < self.lance_menor):
                self.lance_menor = lance.valor


murillo = Usuario("Murillo")
thiago = Usuario("Thiago")
luiz = Usuario("Luiz")

lance_do_thiago = Lances(thiago, 950)
lance_do_murillo = Lances(murillo, 1000)
lance_do_luiz = Lances(luiz, 800)

leilao = Leilao("Carros")

leilao.propoe(lance_do_thiago)
leilao.propoe(lance_do_murillo)
leilao.propoe(lance_do_luiz)

for lance in leilao.lances:
    print("{} | {} R$".format(lance.usuario.nome, lance.valor))

avalia_leilao = Avaliador2()

avalia_leilao.avalia(leilao)

print(avalia_leilao.lance_menor)
print(avalia_leilao.lance_maior)