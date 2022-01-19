#AULA FINAL CURSO 3 PYTHON ALURA
#MÉTODOS PRIVADOS E MÉTODOS ESTÁTICOS

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando conta de {}".format(titular))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor
        print("Depositado{} R$ na conta de {}".format(valor, self.__titular))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Sacado {} R$ da conta de {}".format(valor, self.__titular))
        else:
            print("Transação bloqueada, o limite desta conta foi excedido")


    def transfere(self, valor, destino):
        if(self.__pode_sacar(valor)):
            self.saca(valor)
            destino.deposita(valor)
        else:
            print("Transferencia bloqueada")

    def extrato(self):
        print("O extrato da conta {} é {} R$".format(self.__numero, self.__saldo))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

