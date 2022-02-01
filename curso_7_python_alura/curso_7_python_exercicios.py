#EXERCÍCIOS CURSO 7 PYTHON ALURA

from abc import ABCMeta, abstractmethod
from functools import total_ordering

@total_ordering
class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def conta_proximo_mes(self):
        pass

    def __str__(self):
        return ">> Conta: {} | Saldo: {} <<".format(self._codigo, self._saldo)

    def __eq__(self, other):
        if(type(other)!= Conta):
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if(self._saldo != other._saldo):
            return self._saldo < other._saldo

        return self._codigo < other._codigo

class ContaCorrente(Conta):

    def conta_proximo_mes(self):
        self._saldo *= 1.01

    def __eq__(self, other):
        if (type(other) != Conta):
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if (self._saldo != other._saldo):
            return self._saldo < other._saldo

        return self._codigo < other._codigo

conta_1 = ContaCorrente(1)
conta_2 = ContaCorrente(2)
conta_3 = ContaCorrente(2)
conta_4 = ContaCorrente(50)
conta_5 = ContaCorrente(35)

contas = [conta_1,conta_2,conta_3,conta_4,conta_5]

for conta in sorted(contas):
    print(conta)

numeros = {1,2,3,4,5,6,7,8,9}
numeros_i = {1,3,5,7,9}

print(numeros & numeros_i)
print(numeros | numeros_i)
print(numeros ^ numeros_i)
print(5 in numeros_i)
print(numeros - numeros_i)