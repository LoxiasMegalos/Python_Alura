import numpy as np
import array as arr

numeros_np = np.array([1.3 , 35.9])
numeros_arr = arr.array('d' ,[1.7, 3.5])

print(numeros_np)
print(numeros_arr)

from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

    def __init__(self, numero):
        self._numero = numero
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "Conta: {}, Saldo: {}".format(self._numero, self._saldo)

class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 10

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.02
        self._saldo -= 5

class ContaInvestimento(Conta):

    def passa_o_mes(self):
        pass

    pass

conta_murillo = ContaPoupanca(1)
conta_julia = ContaCorrente(2)
conta_murillo.deposita(9000)
conta_julia.deposita(300)
contas = [conta_murillo, conta_julia]

for conta in contas:
    conta.passa_o_mes()
    print(conta)

conta_edna = ContaInvestimento(12)

class ContaSalario:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "Conta: {}, Saldo: {}".format(self.codigo, self.saldo)

    def __eq__(self, outro):
        if (type(outro) != ContaSalario):
            return False
        return self.codigo == outro.codigo and self.saldo == outro.saldo

class ContaMultiploSalario(ContaSalario):
    pass

conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

print(conta1 == conta2)

contas = [conta1]

print(conta1 in contas)
print(conta2 in contas)

conta3 = [1, 200]

print(conta1 == conta3)

conta4 = ContaMultiploSalario(37) #Um objeto em um filho pode ser igual ao objeto do tipo mãe

print(conta4 == conta1)

print(isinstance(ContaMultiploSalario(37), ContaSalario)) #o objeto do tipo filho é do tipo mãe também