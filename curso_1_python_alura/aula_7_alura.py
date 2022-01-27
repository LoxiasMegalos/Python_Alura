#Alura_aula_7_curso_1_Python
#Números aleatorios - Random

def jogar():

    import random

    print("*******************************************", end="\n")
    print("Bem vindo ao jogo de adivinhação!", end="\n")
    print("*******************************************")

    total_de_rodadas = 0
    numero_secreto = random.randrange(1,101)
    pontos = 1000

    print(numero_secreto)

    print("QUAL NIVEL DE DIFICULDADE DESEJADO?")
    print("(1) Fácil (2) Médio (3) Díficil")

    x = 0
    while(x != 1):
        nivel = int(input("Defina o Nível: "))
        if(nivel == 1 or nivel == 2 or nivel == 3):
            x = 1

    if(nivel == 1):
        total_de_rodadas = 20
    elif(nivel == 2):
        total_de_rodadas = 10
    else:
        total_de_rodadas = 5


    #for rodada in range(1, total_de_rodadas + 1):
    rodada = 1
    while( rodada <= total_de_rodadas):
        print("rodada {} de {}".format(rodada, total_de_rodadas))

        chute_str = input("Digite um numero: ")
        print("Voce digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("VOCE DEVE DIGITAR UM NUMERO ENTRE 1 E 100")
            rodada += 1
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("VOCE ACERTOU! e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("VOCE ERROU, O SEU CHUTE FOI MAIOR QUE O NUMERO SECRETO :(")
            elif(menor):
                print("VOCE ERROU, O SEU CHUTE FOI MENOR QUE O NUMERO SECRETO :(")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(rodada == total_de_rodadas):
                print("VOCE NÃO ACERTOU O NUMERO SECRETO, ERA {}, E VOCE TERMINOU O JOGO COM {} PONTOS!". format(numero_secreto,pontos))
            rodada += 1


    print("FIM DE JOGO!")

if (__name__ == "__main__"):
    jogar()