#Alura_aula_3_curso_1_Python
#If e While

print("*******************************************", end="\n")
print("Bem vindo ao jogo de adivinhação!", end="\n")
print("*******************************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas), end="\n")
    chute_str = input("Digite o seu numero: ")
    print("Você digitou:",chute_str, end="\n")
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        total_de_tentativas = 0
    else:
        if(maior):
            print("Você errou, o seu chute foi maior que o numero secreto!")
        elif(menor):
            print("Você errou, o seu chute foi menor que o numero secreto!")
    rodada = rodada + 1

print("FIM DE JOGO", end="\n")

