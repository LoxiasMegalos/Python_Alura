#VARIAÇÃO DE DICIONÁRIOS

numeros = [1,2,3,4,5,6,7,8,9,0]
numeros_p = [0,2,4,6,8]
numeros_i = [1,3,5,7,9]
set_n = set(numeros)
set_p = set(numeros_p)
set_i = set(numeros_i)

#for numero in set_n:
#    print(numero)

print(set_i | set_p)
print(set_i & set_p)
print(set_n ^ set_p)
print(set_n - set_i)
print(6 in set_p)
print(len(set_n))
print(set_n)
set_n.add(10)
print(len(set_n))
print(set_n)
print(type(set_n))
print(type(frozenset(set_n)))

string = "oi eu sou o goku e eu sou muito forte oi eu amo comer frutas e frutas sao muito forte"
string_lista = string.split()
print(string_lista)
string_set = set(string_lista)
print(string_set)

#Dicionários

dicionario = {"a":1, "b":5, "c":9, "d":13, "e":17}
print(dicionario)
dicionario = dict(f=10,g=15,h=20,i=25,j=30)
print(dicionario)
dicionario["k"] = 35
print(dicionario)
del dicionario["k"]
print(dicionario)
dicionario["j"] = 31
print(dicionario)
print(dicionario.get("j"))
print(dicionario.get("k",0))
print(dicionario.get("m",00))

for elemento in dicionario.items():
    print(elemento)

for termo, numero in dicionario.items():
    print(termo,"é", numero)

for elemento in dicionario.keys():
    print(elemento)

for valor in dicionario.values():
    print(valor)

lista_keys = ["letra {}".format(letra) for letra in dicionario.keys()]
print(lista_keys)
lista_valores_vezes_10 = [10 * valor for valor in dicionario.values()]
print(lista_valores_vezes_10)

#Default Dict

string = "oi eu sou o goku e eu sou muito forte oi eu amo comer frutas e frutas sao muito forte"
string_lower = string.lower()
aparicoes ={}
for palavra in string_lower.split():
    ate_agora = aparicoes.get(palavra,0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in string_lower.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

dicionario = defaultdict(int)
print(dicionario["murillo"])

dicionario["murillo"] = 21
print(dicionario["murillo"])


aparicoes = defaultdict(int)
for palavra in string_lower.split():
    aparicoes[palavra] += 1

print(aparicoes)

class Conta:
    def __init__(self):
        print("Criando uma conta em {}".format(self))

contas = defaultdict(Conta)
contas[15]
contas[17]
contas[19]

from collections import Counter

aparicoes = Counter(string_lower.split())
print(aparicoes)