#AULA 1 - LAÇO WHILE e operador not para inverter um valor bool
#AULA 2 - Laços com strings e funções built ins

#find

palavra = "aluracursos"
print(palavra.find("l"))
print(palavra.find("a"))
print(palavra.find("b"))

palavra = "terra"

index = 0
for letra in palavra:
    if(letra):
        print("A letra {} representa a posição {} da string".format(letra,index))
    index = index + 1

print()
palavra = "Alura"
ref = 0
for artel in palavra:
    if("l" == artel):
        print("Achou a letra {} na posição {}".format(artel, ref))
    ref = ref + 1

a = "cavalo"
b = "baleia"
print()
print("{1} e {0}".format(a,b))
print()

palavra = "testando_tudo"
print(palavra.endswith("do"))
print(palavra.startswith("tes"))
print(palavra.capitalize())
print(palavra.upper())
print(palavra.lower())
print()

#LISTAS []
valores = []
print(type(valores))

frutas = ['banana', 'maca', 'pera', 'uva', 'melancia', 'jamelao']

fruta_pedida = "banana" #input("Qual a fruta que deseja consultar? ")

if(fruta_pedida in frutas):
    print("Sim, temos {}".format(fruta_pedida))
else:
    print("Não temos {}, só temos: {}".format(fruta_pedida, frutas))
print()

precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026 ]
print(min(precos))
print()

funcionarios = ['Astrid','Flavia','Talia', 'Mauricio', 'Waldemar', 'Marina']
print(funcionarios)
print(len(funcionarios))
print()

colocacao = ['Drible da Emoção', 'Bruxos como Ronaldinho', 'Só golaço', '3x1 não é goleada']
campeao = colocacao[1]
print(' O grande campeão do torneio é o time ' + campeao)
print()

lista = [1,1,1,1,1,2,3,4,5]
print("O numero 1 aparece {} vezes na lista".format(lista.count(1)))
print("O _ aparece {} vezes na lista".format(lista.count("_")))
print(lista.index(1))
print(lista.pop())
lista.append(999)
print(lista)
del(lista[5])
print(lista)

if(lista.count("_") == 0):
    print("O programa vai dar certo")
print()

#TUPLAS - LISTAS IMUTÁVEIS

tupla_string = ("a", "b")
tupla_int = (1,2,3,4,5)
print(tupla_string)
print(tupla_int)

print(type(tupla_string))
print(type(tupla_int))

print(min(tupla_int))
print(max(tupla_string))
print(len(tupla_int))

#tupla_string = tupla_string.pop()
#tupla_int = tupla_int.append(6)
#print(tupla_string)
#print(tupla_int)

p1 = (3,5)
p2 = (4,6)
p3 = (5,7)
linha = [p1, p2, p3]
print(linha)
print(linha.pop())
print(linha)
print(linha[0])
print(linha[0][1])
print()
palavras = []
palavras.append("x")
palavras.append("y")
nova = tuple(palavras)
print(nova)
outra = list(nova)
print(outra)
print()

numeros = (1,2,3)
numeros = list(numeros)
numeros.append(45)
print(numeros)
numeros = tuple(numeros)
print(numeros)
print()

#SET
set_numeros = {1453,6342,3131,4467478,5345345}
print(set_numeros)
set_numeros.add(6)
print(set_numeros)
set_numeros.add(1)
print(set_numeros)
print()

for numeros in set_numeros:
    print(numeros)
print()

#DICIONARIOS
dicionario_strings = {"Murillo" : 21, "Julia" : 18, "Edna" : 57}
print(dicionario_strings["Murillo"])
print()
dicionario_ints = {1 : 21, 2 : 18, 3 : 57}
print(dicionario_ints[3])
print()
dicionario_letras = {"a" : "b", "c" : "d", "e" : "f"}
print(dicionario_letras["a"])
print()

#TOTAL DE CARACTERES EM UM LOOP

total = 0
palavra = "Python rocks!"
acabou = False
print(len(palavra))
while(not acabou):
    acabou = (total == len(palavra))
    total = total + 1

print(total - 1)

passos = 0
while (passos <= 9):
    passos += 1
print(passos)

frutas = ["maçã", "banana", "laranja", "melancia"]
print(frutas)
frutas_c = [fruta.upper() for fruta in frutas]
print(frutas_c)

inteiros = [1,3,4,5,7,8]
print(inteiros)

quadrados = [ inteiro*inteiro for inteiro in inteiros]
print(quadrados)

inteiros = [1,3,4,5,7,8,9]
print(inteiros)
pares = [ n for n in inteiros if n % 2 == 0]
print(pares)

#ARQUIVOS

with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha.strip())