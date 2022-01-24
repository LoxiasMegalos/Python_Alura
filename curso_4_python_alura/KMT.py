class KMT:

    def __init__(self, nome, top, jg, mid, adc, sup):
        print("Criando objeto..., time {}".format(nome))
        self.__nome = nome
        self.__top = top
        self.__jg = jg
        self.__mid = mid
        self.__adc = adc
        self.__sup = sup



    def imprime_time(self):
        print("Time: {}".format(self.__nome))
        print("Top: {}".format(self.__top))
        print("Jg : {}".format(self.__jg))
        print("Mid: {}".format(self.__mid))
        print("Adc: {}".format(self.__adc))
        print("Sup: {}".format(self.__sup))

    @property
    def mid(self):
        return self.__mid

    @property
    def top(self):
        return self.__top

    @property
    def jg(self):
        return self.__jg

    @property
    def adc(self):
        return self.__adc

    @property
    def sup(self):
        return self.__sup

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, time):
        self.__nome = time

    def __verifica_jogador(self, nome):

        if(nome == self.__top or nome == self.__jg or nome == self.__mid or nome == self.__adc or nome == self.__sup):
            return True
        else:
            return False

    def selecione_mvp(self, nome):
        if(self.__verifica_jogador(nome)):
            print("{} é o MVP!".format(nome))
        else:
            print("Jogador não encontrado")

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor
        print("Foi depositado na conta de {} {} R$".format(self.__titular, valor))

    def saca(self, valor):
        if(self.__verifica_saldo(valor)):
            self.__saldo -= valor
        else:
            print("Transação Não Efetuada, limite atingido")

    def __verifica_saldo(self, valor):
        if(valor > self.__saldo + self.__limite):
            return False
        else:
            return True

    def extrato(self):
        print("O seu extrato é de: {} R$".format(self.__saldo))

    def transfere(self, valor, destino):
        if(self.__verifica_saldo(valor)):
            self.saca(valor)
            destino.deposita(valor)
        else:
            print("Transferencia rejeitada, limite atingido")


    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor


class Jogadores():

    def __init__(self, jogador):
        self.jogador = jogador

    def __str__(self):
        return self.jogador

    def __eq__(self, other):
        return self.jogador == other.jogador

yang = Jogadores("Yang")
zeeq = Jogadores("Zeeq")

meus_jogadores = [yang, zeeq]

for jogador in meus_jogadores:
    print(jogador)


def tenho_jogador(jogador):
    #for player in meus_jogadores:
        #if jogador == player:
            #return True
    #return False
    return jogador in meus_jogadores


jogador_procurado = Jogadores("Zetty")
print(tenho_jogador(jogador_procurado))