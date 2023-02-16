class Elemento:

    def __init__(self, numero, simbolo, nome, peso):
        self._numero = numero
        self._simbolo = simbolo
        self._nome = nome
        self._peso = peso

    @property
    def numero(self):
        return self._numero

    @property
    def simbolo(self):
        return self._simbolo

    @property
    def nome(self):
        return self._nome

    @property
    def peso(self):
        return self._peso

    def __str__(self):
        return "Numero: {} Simbolo: {} Nome: {} Peso: {}".format(self._numero, self._simbolo, self._nome, self._peso)




Hidrogenio = Elemento(1, "H", "Hidrogenio", 1)
print(Hidrogenio)
