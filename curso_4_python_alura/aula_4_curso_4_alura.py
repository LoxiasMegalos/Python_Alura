#QUANDO NÃO UTILIZAR HERANÇA
import random

class Programas:

    atributo_da_classe = "Eu sou um atributo da classe"
    tempo = 12

    @classmethod
    def class_method(cls):
        return "{} Deu certo!".format(cls.atributo_da_classe)

    @staticmethod
    def teste_static_method():
        return "Você imprimiu um método estático dentro de uma classe"

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

    def __str__(self):
        return "N: {} A: {} L: {}".format(self._nome, self.ano, self._likes)

###################################################################################################
class Filmes(Programas):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print("N: {} A: {} D: {} L: {}".format(self._nome, self.ano, self.duracao,
                                               self._likes))

    def __str__(self):
        return "N: {} A: {} D: {} L: {}".format(self._nome, self.ano, self.duracao, self._likes)

    def horas(self):
        tempo = self.duracao / 60
        inicio = super().tempo
        fim = tempo + inicio
        print("O filme irá começar as {} horas, terá duração de {} horas e irá terminar as {} horas".format(inicio, tempo , fim))
###################################################################################################

class Series(Programas):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print("N: {} A: {} T: {} L: {}".format(self._nome, self.ano, self.temporadas, self._likes))

    def __str__(self):
        return "N: {} A: {} T: {} L: {}".format(self._nome, self.ano, self.temporadas, self._likes)

###################################################################################################

class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        #super().__init__(programas)
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


vingadores = Filmes("vingadores o fim do mundo", 2019, 120)
peakyblinders = Series("peaky blinders", 2015, 5)
tmep = Filmes("todo mundo em panico", 1999, 100)
demolidor = Series("demolidor", 2016, 2)

for i in range(0,10):
    vingadores.dar_likes()

for i in range(0,13):
    tmep.dar_likes()

for i in range(0,16):
    demolidor.dar_likes()

y = 0
c = 0
while(y == 0):
    peakyblinders.dar_likes()
    c += 1
    if(c == 32):
        y = random.randint(1, 1000)

filmes_e_series = [vingadores, peakyblinders, tmep]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print("Tamanho do playlist: {} programas".format(playlist_fim_de_semana.tamanho), end = "\n\n")

for programa in playlist_fim_de_semana.listagem:
    print(programa, end="\n\n")

print(demolidor in playlist_fim_de_semana.listagem, end="\n")

