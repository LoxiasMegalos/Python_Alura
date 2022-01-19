#AULA 5 DO CURSO 3 DE PYTHON ALURA

# PROPRIEDADES | GETTERS | SETTERS

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Salvando a conta de {1} em {0}".format(self, titular))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor
        print("Você depositou {} R$ na conta de {}".format(valor, self.__titular))

    def saca(self, valor):
        ref = self.__saldo - valor

        if(ref >= - self.__limite):
            self.__saldo -= valor
            print("Você sacou {} R$".format(valor))
        else:
            print("Transação bloqueada, o limite dessa conta é de {} R$ e este saque de {} R$ deixaria a conta {} R$ negativos ". format(self.__limite, valor, self.__saldo - valor))

    def extrato(self):
        print("O seu extrato é: {} R$".format(self.__saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return print("{} R$".format(self.__limite))

    @limite.setter
    def limite(self, limite):
        self.__limite = limite