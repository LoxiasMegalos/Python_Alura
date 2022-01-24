#HERANÇA MULTIPLA

class Programas:

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

class Filmes(Programas):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


    def __str__(self):
        return "N: {} A: {} D:{}min L: {}".format(self._nome, self.ano, self.duracao, self._likes)

class Series(Programas):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return "N: {} A: {} T: {}temps L: {}".format(self._nome, self.ano, self.temporadas, self._likes)

class Playlist:

    def __init__(self, nome, listagem):
        self.nome = nome
        self._listagem = listagem

    def __getitem__(self, item):
        return self._listagem[item]

    def __len__(self):
        return len(self._listagem)

    def __add__(self, other):
        self._listagem.extend(other)

v = Filmes("vingadores o filme", 2012, 120)
k = Filmes("A voz do silencio", 2017, 129)
x = Series("vingadores a serie", 2012, 2)
y = Series("serie mais braba de todas", 2010, 9)

Play = [v, k, x, y]

playlist_semana = Playlist("Playlist Gostosa", Play)

b = Filmes("quero adicionar na playlist", 2010, 200)

#playlist_semana.__add__([b])

playlist_semana + [b]

#for programa in playlist_semana:
#    print(programa)
#print(len(playlist_semana))
#print(playlist_semana[4])

class Jogador:

    def reconhecer(self):
        print("Você é um jogador")

    def __init__(self, nome):
        self.nome = nome

class KMT(Jogador):
    def reconhecer(self):
        print("Você é um KMT!")

    def campeonato(self):
        print("Bem vindo aos KMTS!")

class TMK(Jogador):
    def reconhecer(self):
        print("Você é um TMK")

    def campeonato(self):
        print("Bem vindo aos TMKS!")

class prefixo:
    def __str__(self):
        return "KMT {}".format(self.nome)

class Normal(KMT):
    pass
class NNormal(KMT, TMK, prefixo):
    pass

enzet = NNormal("Zetty")
print(enzet)