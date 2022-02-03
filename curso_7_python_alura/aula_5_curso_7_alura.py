#CONJUNTOS - SETS

from collections import Counter
from collections import defaultdict
from typing import List, Tuple, Any

numeros = [0,1,2,3,4,5,6,7,8,9]
pares = [0,2,4,6,8]
impares = [1,3,5,7,9]

n_set = set(numeros)
p_set = set(pares)
i_set = set(impares)
print(n_set)
print(p_set)
print(i_set)
print(p_set | i_set)
print(p_set & i_set)
print(n_set ^ p_set)
print(n_set - i_set)
print(5 in p_set)
print(5 in i_set)

print(type(n_set))
f_n_set = frozenset(n_set)
print(type(f_n_set))

p_set.add(10)
print(p_set)
p_set.remove(10)
print(p_set)

for numero in n_set:
    print(numero)

string = "oi eu sou oi eu sou murillo oi eu amo neve eu sou murillo"
string_l = string.split()
string_set = set(string_l)
print(string_l)
print(string_set)

dicionario = dict(oi = 1, tudo = 2, bem = 50, e = 35, voce = 70)
print(dicionario.get("teste",0))
dicionario["teste"] = 80
print(dicionario)
del dicionario["teste"]
print(dicionario)

for elemento in dicionario:
    print(elemento)

for elemento in dicionario.keys():
    print(elemento)

for elemento in dicionario.values():
    print(elemento)

for elemento in dicionario.items():
    print(elemento)

for termo, valor in dicionario.items():
    print(valor)

dicionario_termos = ["oi {}".format(elemento) for elemento in dicionario.keys()]
print(dicionario_termos)

dicionario_valores = [10 + valor for valor in dicionario.values()]
print(dicionario_valores)

string_lower = string.lower()
print(string_lower)
aparicoes = {}

for palavra in string_lower.split():
    ate_agora = aparicoes.get(palavra,0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

aparicoes = defaultdict(int)

for palavra in string_lower.split():
    aparicoes[palavra] += 1

print(aparicoes)

class Conta:
    def __init__(self):
        print("Criando conta em {}".format(self))

contas = defaultdict(Conta)

contas[1]
contas[2]

print(contas)

aparicoes = Counter(string_lower.split())
print(aparicoes)

#TESTANDO O USO DE DIVERSAS COLEÇÕES

texto_1 = """
Olá, Dev! Você provavelmente deve ter se questionado como é possível fixar uma lista lateral no canto da tela, ou como fixar um menu no topo independente da barra de rolagem, até mesmo como conseguir posicionar um elemento tendo outro como referência. Com a propriedade position, é possível fazer isso e muito mais! Neste artigo vamos aprender sobre cada uma das suas possibilidades de uso.

Position significa posição em português. O posicionamento padrão de todo elemento no HTML é estático, ou seja, possui o valor position: static, mesmo que este valor não tenha sido declarado. Todo elemento estático é posicionado alinhado pelo canto superior esquerdo no corpo do documento. Não sendo possível alterar sua posição. Esta é a posição 0 de um elemento no corpo do documento, segundo as coordenadas do HTML.
E agora? Como posso alterar a posição de um elemento?

Para alterarmos a posição de um elemento é preciso primeiro modificar o seu valor que vem por padrão: static. Para a propriedade position, é possível atribuir 5 valores, que são: static, fixed, sticky, relative e absolute.
"""
texto_2 = """
Estava eu, estudando novamente o framework Laravel do mundo PHP - depois de algum tempo muito focado no Java e usando o Intellij como editor de código favorito – e percebi uma coisa: a utilização do debug não é bem explicada... vocês já perceberam isso? No meu caso, o debug foi, e é, imprescindível quando estou no Java. Portanto, partindo dessa percepção inicial, este artigo mostrará como podemos fazer debug da aplicação Laravel nos editores da Jetbrains. Bora lá?

Alguns pontos importantes a serem destacados
O primeiro ponto que é preciso destacar é que daqui em diante vamos nos referir aos editores Intellij Idea ou PHP Storm apenas como como “editor”, já que o que vamos abordar neste artigo funciona tanto para o Intellij Idea quanto para o PHP Storm.

Outro ponto importante é que vamos precisar instalar apenas uma ferramenta no sistema operacional. Durante este artigo vamos utilizar o Linux, mais especificamente o Ubuntu 20.04, que é o sistema que utilizo atualmente, mas você pode utilizar os links abaixo, para realizar as instalações no Windows e ou no macOS respectivamente:
"""

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia/total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.1f}%".format(caractere, proporcao*100))

analisa_frequencia_de_letras(texto_1)
print("texto 2: ")
analisa_frequencia_de_letras(texto_2)