#ORDENAÇÃO TOTAL - FUNCTOOLS

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
    def proximo_mes(self):
        pass

    def __str__(self):
        return ">> Conta: {} | Saldo: {} <<".format(self._codigo, self._saldo)

    def __eq__(self, other):
        if(type(other) != Conta):
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo


class ContaCorrente(Conta):

    def proximo_mes(self):
        pass

    def __eq__(self, other):
        if(type(other) != ContaCorrente):
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo



conta_1 = ContaCorrente(1)
conta_2 = ContaCorrente(1)
conta_3 = ContaCorrente(40)
conta_3.deposita(1000)
conta_4 = ContaCorrente(15)
conta_4.deposita(1000)
conta_5 = ContaCorrente(145)

contas = [conta_1, conta_2, conta_3, conta_4]

print(conta_1)
print("Comparando se duas contas são iguais: ", conta_1 == conta_2)
print("Testano o método lt da classe mãe:", conta_1 > conta_3)

for conta in sorted(contas):
    print(conta)


#Ordenando classe pelo método de funções:



class ContaSemLT:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return ">> Conta: {} | Saldo: {} <<".format(self._codigo, self._saldo)

    def __eq__(self, outro):
        if(type(outro) != ContaSemLT):
            return False
        return self._saldo == outro.saldo and self._codigo == outro._codigo


conta_murillo = ContaSemLT(10)
conta_julia = ContaSemLT(11)
conta_murillo.deposita(100)
conta_julia.deposita(200)
conta_edna = ContaSemLT(5)
conta_edna.deposita(999)
conta_eduardo = ContaSemLT(4)
conta_eduardo.deposita(50)

contas_lt = [conta_julia, conta_murillo, conta_eduardo, conta_edna]

def extrai_saldo(conta):
    return conta._saldo

print("Ordenando objetos sem o método LT - UTILIZANDO FUNÇÃO - acessando possíveis atributos privados")
for conta in sorted(contas_lt, key=extrai_saldo):
    print(conta)

print("Ordenando objetos sem o método LT - UTILIZANDO ATTRGETTER -acessando possíveis atributos privados")
from operator import attrgetter
for conta in sorted(contas_lt, key=attrgetter("_saldo")):
    print(conta)

#for indice in range(len(contas_lt)):
#    print(indice, contas_lt[indice])

print("Forçando a lista em um enumerate para me dar tuplas: ")
tuplas_lt = list(enumerate(contas_lt))
print(tuplas_lt)
for indice, conta in tuplas_lt:
    print(conta)

#FUNCTOOLS

conta_x = ContaSemLT(10)
conta_y= ContaSemLT(11)
conta_x.deposita(100)
conta_y.deposita(100)
conta_z = ContaSemLT(5)
conta_z.deposita(100)
conta_c = ContaSemLT(4)
conta_c.deposita(100)

contas_attrgetter = [conta_x, conta_y, conta_z, conta_c]

from operator import attrgetter
for conta in sorted(contas_attrgetter, key=attrgetter("_saldo", "_codigo")):
    print(conta)


#from functools import total_ordering
print(conta_5 <= conta_1)
print(conta_1 <= conta_2)
print(conta_1 < conta_1)
print(conta_1 <= conta_1)