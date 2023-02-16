
class JogaYJoga:

    def __init__(self):
        print("Criando objeto em {}".format(self))
        self = " "

    def imprime_joga(self):
        print("Joga Y Joga")
        print()

joga = JogaYJoga()
joga.imprime_joga()

joga_2 = JogaYJoga()
joga.imprime_joga()

class Carro:

    def __init__(self):
        print("Criando objeto em {0}".format(self))
        #self.nome = nome
        #self.modelo = modelo
        #self.cor = cor

    def imprime_carro(self):
        print("{} tem um {} {}".format(self.nome, self.modelo, self.cor))
        print()

    def cria_carro(self):
        self.nome = input("Digite seu nome: ")
        self.modelo = input("Digite o modelo: ")
        self.cor = input("Digite a cor: ")


carro = Carro()
carro.cria_carro()
carro.imprime_carro()

teste = carro
teste.imprime_carro()
#carro = None
#print(carro)
#print(type(carro))

carro1 = Carro()
carro.cria_carro()
carro.imprime_carro()

