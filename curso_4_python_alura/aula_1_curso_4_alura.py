# PRIMEIRA AULA DO CURSO 4 DE PYTHON NA ALURA
# AVANÇANDO NA ORIENTAÇÃO A OBJETOS

print("Curso 4 de Python na ALura - Avançando na Orientação a objetos!")


class PlaylistFilmes:

    def __init__(self, nome, ano, duracao):
        print("Adicionando Filme: {} ".format(nome))
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class PlaylistSeries:

    def __init__(self, nome, ano, temporadas):
        print("Adicionando Série: {} ".format(nome))
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = PlaylistFilmes("Vingadores - Guerra Infinita", 2018, 160)
print(
    "Nome: {} - Ano: {} - Duração: {} minutos - Likes: {} ".format(vingadores.nome, vingadores.ano, vingadores.duracao,
                                                                   vingadores.likes))

atlanta = PlaylistSeries("Atlanta", 2018, 2)

atlanta.dar_like()
atlanta.dar_like()
atlanta.nome = "senhor dos aneis"
print("Nome: {} - Ano: {} - Número de Temporadas: {} - Likes: {} ".format(atlanta.nome, atlanta.ano, atlanta.temporadas,
                                                                          atlanta.likes))
print(atlanta.likes)

print(__name__)