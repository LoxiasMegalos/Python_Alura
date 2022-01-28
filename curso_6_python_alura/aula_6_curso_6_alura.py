#ORDEM NATURAL

from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @property
    def saldo(self):
        return self._saldo

    @abstractmethod
    def proximo_mes(self):
        pass

    def __str__(self):
        return "Conta: {}, Saldo: {}".format(self._codigo, self._saldo)

    def __eq__(self, other):
        if(type(other) != Conta):
            return False

        return self._saldo == other._saldo and self._codigo == other._codigo

    def __len__(self):
        return len(self._codigo)

class ContaPoupanca(Conta):

    def proximo_mes(self):
        self._saldo *= 1.019
        self._saldo -= 20

    def __eq__(self, other):
        if(type(other) != ContaPoupanca):
            return False

        return self._saldo == other._saldo and self._codigo == other._codigo


class ContaC(Conta):

    def proximo_mes(self):
        pass

    pass

conta_1 = ContaPoupanca(1)
conta_2 = ContaPoupanca(1)
conta_3 = ContaC(2)

contas = [conta_1, conta_2, conta_3]

for conta in contas:
    conta.proximo_mes()
    print(conta)

# TUPLAS

for indice in range(len(contas)):
    print(indice, contas[indice])

tuplas = list(enumerate(contas))
print(tuplas)

for tupla in tuplas:
    print(tupla)

for _, conta in tuplas:
    print(conta)

for indice, _ in tuplas:
    print(indice)

# ORDENAÇÃO BÁSICA

idades = [65, 23, 12, 243, 78, 15, 5, 1, 19]

print(idades)
print(sorted(idades))
print(sorted(idades, reverse=True))
print(list(sorted(reversed(idades))))
print(list(reversed(sorted(idades))))
print(idades)
idades.sort()
print(idades)
idades.reverse()
print(idades)

#ORDENAÇÃO DE OBJETOS SEM ORDEM NATURAL

#Reverse - Lazy
#Sorted - in Place

class ContaSalario:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __eq__(self, other):
        if(type(other) != ContaSalario):
            return False
        return self.saldo == other.saldo and self.codigo == other.codigo

    def __str__(self):
        return ">> Conta: {} | Saldo: {} <<".format(self.codigo, self.saldo)

    def __lt__(self, other):
        return self.saldo <= other.saldo


conta_murillo = ContaSalario(17)
conta_murillo.deposita(500)
conta_dani = ContaSalario(3)
conta_dani.deposita(1000)
conta_paulo = ContaSalario(133)
conta_paulo.deposita(510)
conta_batman = ContaSalario(18)
conta_batman.deposita(500)

contas = [conta_murillo, conta_dani, conta_paulo]

#ORDENANDO OBJETOS:

print("Ordenando Objetos com funções externas")
def extrai_saldo(conta):
    return conta.saldo
for conta in sorted(contas, key=extrai_saldo): #Ordenando em lista o saldo acessado em cada objeto através da função
    print(conta)
print("Ordenando Objetos com a biblioteca attrgetter")
from operator import attrgetter
for conta in sorted(contas, key=attrgetter("saldo")):
    print(conta)
# Mas, e se os atributos que quero acessar forem privados?
print("Utilizando o método LT na classe Conta Salário")
print(conta_murillo < conta_dani)
print(conta_batman > conta_murillo)
print("Iterando e ordenando uma classe com o método LT implementado usando sorted")
for conta in sorted(contas):
    print(conta)