#ATIVIDADES COMPLEMENTARES AULAS ALURA PYTHON CURSO 1
#***************************************************#

#while
contador = 1
while(contador <= 10):
    print(contador)
    contador= contador + 2
    if(contador == 5):
        contador = contador + 2
print()
#String Interpolation
dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017
print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim), end="\n")
print()

#For

contador_w = 1
while(contador_w <= 10):
    print(contador_w, end="\n")
    contador_w = contador_w + 1
print()
print("O código com for Equivalente é: ", end="\n")
print()
for contador_f in range(1,11):
    print(contador_f)
print()
for contador_3 in range(1,11,3):
    print(contador_3)
print()

#break e continue

i = 1
while(i <= 7):
    print(i)
    i = i + 1
    if(i == 5):
        break

print()
for y in range(1,8):
    if(y == 5):
        continue
    print(y)
print()

#Mais interpolação de Strings
print("Ola Sr. {1} {0}".format("Cordeiro", "Leonardo"))

print("R$ {:7.1f}".format(1000.12))
print("R$ {:07.2f}".format(4.11))
print()

nome = "MATEUS"
print(f"Meu nome é {nome.lower()}")
print()

#RANDOM - NUMEROS ALEATORIOS

import random
print(random.random())
x = random.random()*100
print(x)
print(int(x))
print(round(x), end="\n")
print()

i = 0
while(i != 10):
    random.seed(51421233)
    aleatorio = random.randrange(0,4)
    print(aleatorio)
    i = i + 1

print()

# entendendo funcionalidades python

round(3.5)
round(4.5)

z = 3 / 2
print(z)
z = 7 // 2
print(z)
print()

#FUNÇÕES

def oi_mundo():
    print("Oi Mundo!")
    print()

oi_mundo()
oi_mundo()
oi_mundo()

numero_1 = int(input("Qual o primeiro Numero: "))
numero_2 = int(input("Qual o segundo Numero: "))

def soma(a, b):
    #c = a + b
    return a + b


print(soma(numero_1,numero_2))

