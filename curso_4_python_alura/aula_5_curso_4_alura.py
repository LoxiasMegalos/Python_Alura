#AULA 5 CURSO 4 PYTHON ALURA!
#DUCK TYPING E MODELO DE DADOS
#DUCK TYPING - FAZER CLASSES SE PASSAREM POR UM OBJETO DE DETERMINADO TIPO - EXEMPLO: PASSAR PARA UMA CLASSE UMA LISTA COMO PARAMETRO E FAZER COM QUE ESTA LISTA HERDE OS COMPORTAMENTOS DE UM DETERMINADO TIPO DE ESTRUTURA DE DADOS, COMO UM LISTA OU SEQUÊNCIA DE ITENS ITERÁVEIS
#CLASSES ABSTRATAS ABC

from abc import ABCMeta, abstractmethod

class Programas(metaclass= ABCMeta):

    filme = "Hora de aventura"
    duracao = 2
    horario = 12

    @classmethod
    def verifica_filme(cls):
        return print(cls.filme)

    @staticmethod
    def agradecimento():
        return print("Obrigado por assistir a emissora mais foda do Brasil")

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

    @abstractmethod
    def __str__(self):
        return "Nome : {} Ano: {} Likes: {}".format(self._nome, self.ano, self._likes)


class Filmes(Programas):

    def __init__(self, nome, ano, duracao):
        self.duracao = duracao
        super().__init__(nome, ano)

    def __str__(self):
        return "Nome : {} Ano: {} Duração: {} Likes: {}".format(self._nome, self.ano, self.duracao,self._likes)

    def hora_de_inicio(self):
        tempo = self.duracao / 60
        print("O filme atual é {} que teve inicio as {} horas e sua duracao é de {} horas, o próximo filme será {}, com inicio as {} com duração de {} horas".format(super().filme, super().horario, super().duracao, self.nome, super().horario + super().duracao,tempo))


class Series(Programas):

    def __init__(self, nome, ano, temporadas):
        self.temporadas = temporadas
        super().__init__(nome, ano)

    def __str__(self):
        return "Nome : {} Ano: {} Temporadas: {} Likes: {}".format(self._nome, self.ano, self.temporadas, self._likes)


class Playlist:

    def __init__(self, nome, playlist):
        self.nome = nome
        #super().__init__(playlist)
        self._playlist = playlist

    def __getitem__(self, item):
        return self._playlist[item]

    def __len__(self):
        return len(self._playlist)

    @property
    def listagem(self):
        return self._playlist

    def __add__(self, other):
        self._playlist.extend(other)


if(__name__ == "__main__"):

    v = Filmes("vingadores", 2018, 120)
    t = Series("Better Call Saul", 2015, 3)

    for x in range(0,32):
        t.dar_likes()
        v.dar_likes()

    Play = [v, t]

    #for programa in Play:
        #print(programa)

    playlist_teste = Playlist("teste", Play)

    print(len(playlist_teste))
    #print(len(playlist_teste))

    for programa in playlist_teste:
        print(programa)

    #print(t in playlist_teste)
    #print(playlist_teste[0])
    #print(t in playlist_teste)

    #v.verifica_filme()

    #v.hora_de_inicio()

    #v.agradecimento()
    print()

    y = Series("Better Call murillo", 2015, 2)
    playlist_teste.__add__([y])

    for p in playlist_teste:
        print(p)


