#Alura_aula_6_curso_1_Python
#Números aleatorios - Random

import random

print("*******************************************", end="\n")
print("Bem vindo ao jogo de adivinhação!", end="\n")
print("*******************************************")


total_de_rodadas = 3
#numero_secreto = round(random.random() * 100)
numero_secreto = random.randrange(1, 101)

print(numero_secreto)

for rodada in range(1, total_de_rodadas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_rodadas))
    chute_str = input("Digite um número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)
    #chute = round(random.random() * 100)
    #print("Você digitou: ", chute)

    if(chute < 0 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você Acertou!!")
        break
    else:
        if(maior):
            print("Você errou, o numero digitado era maior que o numero secreto! Você digitou {} quando o numero secreto era {}".format(chute, numero_secreto))
        elif(menor):
            print("Voce errou! O seu chute foi menor que o numero secreto!")

print("FIM DE JOGO!!!!")