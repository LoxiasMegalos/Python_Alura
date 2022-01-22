#AULA 4 DO CUROS 4 DE PYTHON ALURA
#POLIMORFISMO

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

########################################################################################################################
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

########################################################################################################################

class Series(Programas):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print("N: {} A: {} T: {} L: {}".format(self._nome, self.ano, self.temporadas, self._likes))

    def __str__(self):
        return "N: {} A: {} T: {} L: {}".format(self._nome, self.ano, self.temporadas, self._likes)

########################################################################################################################

vingadores = Filmes("vingadores o fim do mundo", 2019, 120)
peakyblinders = Series("peaky blinders", 2015, 5)

for i in range(0,10):
    vingadores.dar_likes()

y = 0
c = 0
while(y == 0):
    peakyblinders.dar_likes()
    c += 1
    if(c == 32):
        y = random.randint(1, 1000)

print("N: {} A: {} D: {} L: {}".format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.likes))

print("N: {} A: {} T: {} L: {}".format(peakyblinders.nome, peakyblinders.ano, peakyblinders.temporadas, peakyblinders.likes))

print()

Playlist = [vingadores, peakyblinders]

print("Imprimindo programa sem atributos especificos: ")
print()
for programa in Playlist:
    print("N: {} A: {} X L: {}".format(programa.nome, programa.ano, programa.likes))

print()
print("Imprimindo programas utilizando a função hasattr")
print()
for programa in Playlist:

    ref = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas                                      #QUERENDO ENTRAR MUITO EM OBJETOS SEM PRECISAR

    if(ref > 10):
        print("N: {} A: {} D: {} L: {}".format(programa.nome, programa.ano, ref, programa.likes))
    else:
        print("N: {} A: {} T: {} L: {}".format(programa.nome, programa.ano, ref, programa.likes))

#CLASSES DEVEM TER COESÃO, FILMES E SÉRIES DEVEM SABER SE IMPRIMIR

print()
print("Imprimindo programas utilizando as fgunções específicas de cada classe pelo método de polimorfismo - imprime é chamado em diferentes classes para cada caso")
print()
for programa in Playlist:
    programa.imprime()

print()
print("Utilizando a Função __str__") #MELHOR OPÇÃO
print()

for programa in Playlist:
    print(programa)

###################################################################################################

print()
print(vingadores.atributo_da_classe)
print(vingadores.class_method())
print(vingadores.teste_static_method())
print()
vingadores.horas()
print(f"Imprimindo um atributo da classe mãe através de um objeto na classe especifica: {vingadores.tempo}")