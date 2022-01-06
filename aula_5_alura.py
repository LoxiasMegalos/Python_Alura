#Alura_aula_3_curso_1_Python
#For

print("*******************************************", end="\n")
print("Bem vindo ao jogo de adivinhação!", end="\n")
print("*******************************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas), end="\n")
    chute_str = input("Digite um número entre 1 e 100: ")
    chute= int(chute_str)
    print("Você digitou: ", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100!", end="\n")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior que o numero secreto!")
        elif(menor):
            print("Voce errou! O seu chute foi menor que o numero secreto!")


print("FIM DE JOGO!", end="\n")