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

from collections import Counter

#def proporcao_texto(texto):
texto_2 = """
Estava eu, estudando novamente o framework Laravel do mundo PHP - depois de algum tempo muito focado no Java e usando o Intellij como editor de código favorito – e percebi uma coisa: a utilização do debug não é bem explicada... vocês já perceberam isso? No meu caso, o debug foi, e é, imprescindível quando estou no Java. Portanto, partindo dessa percepção inicial, este artigo mostrará como podemos fazer debug da aplicação Laravel nos editores da Jetbrains. Bora lá?

Alguns pontos importantes a serem destacados
O primeiro ponto que é preciso destacar é que daqui em diante vamos nos referir aos editores Intellij Idea ou PHP Storm apenas como como “editor”, já que o que vamos abordar neste artigo funciona tanto para o Intellij Idea quanto para o PHP Storm.

Outro ponto importante é que vamos precisar instalar apenas uma ferramenta no sistema operacional. Durante este artigo vamos utilizar o Linux, mais especificamente o Ubuntu 20.04, que é o sistema que utilizo atualmente, mas você pode utilizar os links abaixo, para realizar as instalações no Windows e ou no macOS respectivamente:
"""
def analisa_texto(texto):
    aparicoes = Counter(texto.lower())
    total_aparicoes = sum(aparicoes.values())

    proporcao = [(letra, valor / total_aparicoes) for letra, valor in aparicoes.items()]
    proporcao = Counter(dict(proporcao))
    mais_comuns = proporcao.most_common(10)

    for letra, valor in mais_comuns:
        print("{} => {:.2f}%".format(letra, valor*100))

