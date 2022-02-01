#DICIONÁRIOS

#relembrando conjuntos - SET
#relembrando funções e polimorfismo

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
    def passa_mes(self):
        pass

    def __str__(self):
        return ">> Conta: {} | Saldo: {} <<".format(self._codigo, self._saldo)

    def __eq__(self, outro):
        if type(outro) != Conta:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo

class ContaCorrente(Conta):

    def passa_mes(self):
        pass


conta_1 = ContaCorrente(1)
conta_2 = ContaCorrente(1)
conta_3 = ContaCorrente(50)
conta_4 = ContaCorrente(30)

contas = [conta_1,conta_2,conta_3,conta_4]

conta_2.deposita(50)
contas.remove(conta_1)


numeros = [0,1,2,3,4,5,6,7,8,9]
numeros_pares = [2,4,6,8,0]
numeros_impares = [1,3,5,7,9]

set_numeros = set(numeros)
set_pares = set(numeros_pares)
set_impares = set(numeros_impares)

ou = set_pares | set_impares
print("Ou: ", ou)
e = set_pares & set_impares
print("And e: ", e)
xor = set_pares ^ set_numeros
print("Ou especial: ", xor)
menos = set_numeros - set_pares
print("Conjunto numeros - pares: ", menos)
verifica = 5 in numeros_impares
print("5 in numeros impares? ", verifica)

set_numeros.remove(0)
print(set_numeros)
print(len(set_numeros))
set_numeros.add(0)
print(set_numeros)
print(len(set_numeros))
print(type(set_numeros))
frozen_numeros = frozenset(set_numeros)
print(type(frozen_numeros))

string = "meu cachorro meu gato eu amo meus animais e minha namorada eu amo o mundo e cachorro quente"
lista_string = string.split()
print(lista_string)
set_string = set(lista_string)
print(set_string)

# DICIONÁRIO

print("Dicionário")

aparicoes = {"murillo": 10, "Raissa" : 9, "Julia":3}
print(aparicoes)
print(aparicoes["murillo"])
print(aparicoes.get("edna",0))
print(aparicoes.get("Raissa",0))
aparicoes = dict(oi =1, tudobem=2,evoce = 30, eutobem = 60)
print(aparicoes)
aparicoes["oi"] = 4
print(aparicoes)

del aparicoes["oi"]
print(aparicoes)
print("oi" in aparicoes)

for elemento in aparicoes:
    print(elemento)

#for elemento in aparicoes.keys():
#    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, "=", valor)

aparicoes_lista = ["palavra {}".format(chave) for chave in aparicoes.keys()]
print(aparicoes_lista)

aparicoes_values = [15 + valor for valor in aparicoes.values()]
print(aparicoes_values)

print(aparicoes)
aparicoes["que legal"] = 80
print(aparicoes)