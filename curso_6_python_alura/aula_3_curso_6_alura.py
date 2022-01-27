#AULA 3 - POLIMORFISMO E ARRAYS

#listas

lista = [1,2,3,4,5]
lista2 = [6]
lista.extend(lista2)
lista.insert(0,0)
lista.remove(6)
lista.append(7)
for numero in lista:
    print(numero)
lista.clear()
print(lista)

#tuplas - imutáveis - incapaz de adicionar ou retirar termos, porém posso alterar internamente o valor do atributo desses termos, seja por uma função ou classe

class Conta:

    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "Conta: {}, Saldo: {} R$".format(self.numero, self.saldo)

conta_murillo = Conta(10)
conta_murillo.deposita(100)

conta_julia = Conta(1)
conta_julia.deposita(999)

contas = (conta_murillo,conta_julia)
contas[0].deposita(100)

for conta in contas:
    print(conta)

conta_edna = (100 , 1000)

def altera_tupla_saldo(conta):
    saldo = conta[1] + 100
    return (conta[0], saldo)

conta_edna = altera_tupla_saldo(conta_edna)
print("Conta: {}, Saldo: {}".format(conta_edna[0], conta_edna[1]))

#Polimorfismo e Arrays
from abc import ABCMeta, abstractmethod

class ContaC(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "Conta: {}, Saldo: {} R$".format(self._codigo, self._saldo)

class ContaCorrente(ContaC):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(ContaC):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes() #duck typing
    print(conta)

#Array e Numpy
#Tipo Array deve ser importado - evitaremos utilizar - sendo super específico
#Maior eficácia quando está sendo trabalhado com números
#Falando o tipo e todos os elementos sendo desse tipo

import array as arr

arr.array('d', [1, 3.5])

#operações matemáticas precisas geralmente se utiliza numpy e é evitado utilizar a array nativa do python

import numpy as np

numeros = np.array([1, 3.5]) + 3
print(numeros)

#métodos abstratos

class ContaInvestimento(ContaC):
    pass

print(ContaInvestimento(1))