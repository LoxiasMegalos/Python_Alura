#HERANÇA PARA DUPLICAÇÃO

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

class Filmes(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def retorna_cadastro_diferenciado(self):
        pass


class Series(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas



vingadores = Filmes("vingadores", 2018, 160)
vingadores.nome = "vingadores, Guerra infinita"
twd = Series("the walking Dead", 2012, 9)
vingadores.dar_likes()
vingadores.dar_likes()
twd.dar_likes()


print("N = {} A = {} D = {} L = {}".format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.likes))
print("N = {} A = {} T = {} L = {}".format(twd.nome, twd.ano, twd.temporadas, twd.likes))