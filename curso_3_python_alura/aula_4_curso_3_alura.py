
# ENCAPSULAMENTO
# ATRIBUTOS "PRIVADOS" - __ ANTES DE CADA ATRIBUTOS SÃO AVISOS PARA DEVS, EMBORA AINDA POSSAM SER ALTERADOS.

class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Adicionando a conta {1} em {0}".format(self, numero))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        print("Você está depositando {} R$ na conta nº {} de {}".format(valor, self.__numero, self.__titular))
        self.__saldo += valor

    def saca(self, valor):
        print("Você está sacando {} R$ da conta nº {} de {}".format(valor, self.__numero, self.__titular))
        ref = self.__saldo - valor

        if(ref >= -self.__limite):
            self.__saldo -= valor
        else:
            print("Transação negada, a conta {} tem um limite de {} R$ e com este depósito a conta ficaria com {} R$".format(self.__numero, -self.__limite, ref))

    def extrato(self):
        print("Saldo de {} R$ do titular {}".format(self.__saldo, self.__titular))

    def transfere(self, valor, destino):
        self.saca(valor)
        self.extrato()
        destino.deposita(valor)







class Retangulo:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x*y

    def obter_area(self):
        print("A área do retângulo é de: {} centímetros!".format(self.__area))

