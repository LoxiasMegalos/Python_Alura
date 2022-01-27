#OUTROS BUILTINS

from abc import ABCMeta, abstractmethod

class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    #@abstractmethod
    def conta_proximo_mes(self):
        pass

    def __str__(self):
        return "Conta: {}, Saldo: {}".format(self._codigo, self._saldo)

    def __eq__(self, other):
        if(type(other) != Conta):
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo


class ContaPoupança(Conta):

    def conta_proximo_mes(self):
        self._saldo *= 1.1
        self._saldo -= 20

    def __eq__(self, other):
        if(type(other) != ContaPoupança):
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

class ContaInvestimento(Conta):

    def conta_proximo_mes(self):
        self._saldo -= 100

    def __eq__(self, other):
        if(type(other) != ContaInvestimento):
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

class ContaBonus(Conta):

    def conta_proximo_mes(self):
        pass

    pass


conta_1 = ContaPoupança(1)
conta_2 = ContaPoupança(1)
conta_3 = ContaInvestimento(3)
conta_4 = ContaBonus(4)
conta_5 = Conta(4)
conta_6 = [4,0]
conta_7 = ContaInvestimento(3)


contas = [conta_1,conta_2,conta_3,conta_4,conta_5, conta_7]

for conta in contas:
    conta.conta_proximo_mes()
    print(conta)

print(conta_1 == conta_2)
print(conta_4 == conta_5)
print(conta_7 == conta_3)
print(conta_5 == conta_6)
print(isinstance(conta_4,Conta))

#OUTRAS FUNÇÕES BUILTINS

idades = [15,87,32,65,56,32,49,37] #imprimir de forma elemento - posição 15 - 1 , 87 - 2 etc.
print(range(len(idades)))
#for i in range(len(idades)):
#    print(i, idades[i])

print(enumerate(idades))
print(list(enumerate(idades))) #Forçou a geração dos valores

for indice, idade in enumerate(idades): #unpacking de  um tupla
    print(indice, "x", idade)

#e se estou interessado apenas no primeiro usuario da tupla

usuarios = [("murillo",12,1999), ("julia",13, 42134), ("edna", 13, 1444)]

for nome, _ , _ in usuarios:
    print(nome)

# Ou

for nome, idade, ano in usuarios:
    print(ano)