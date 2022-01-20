#Alura_aula_7_curso_1_Python
#Números aleatorios - Random


def jogar():

    import random

    print("*******************************************", end="\n")
    print("Bem vindo ao jogo da forca!", end="\n")
    print("*******************************************")

    total_de_rodadas = 0
    numero_secreto = random.randrange(1,101)
    pontos = 1000

    print("ESCOLHA O NIVEL DO JOGO")
    print("(1) FÁCIL (2) MÉDIO (3) DIFÍCIL")
    x = True
    while x:
        nivel = int(input("SELECIONE O NIVEL IMEDIATAMENTE: "))
        if (nivel == 1 or nivel == 2 or nivel == 3):
            x = False
        else:
            print("SELECIONE UM NIVEL VALIDO!")

    if (nivel == 1):
        total_de_rodadas = 20
    elif (nivel == 2):
        total_de_rodadas = 10
    else:
        total_de_rodadas = 3

    for rodada in range(1, total_de_rodadas + 1):
        print("Rodada {} de {}".format(rodada, total_de_rodadas))

        chute = int(input("DIGITE UM NUMERO: "))
        if (chute < 1 or chute > 100):
            print("O SEU CHUTE DEVE SER ENTRE 1 E 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("PARABENS VOCE ACERTOU! E TERMINOU O JOGO COM {} PONTOS". format(pontos))
        else:
            if(maior):
                print("VOCE ERROU, O SEU CHUTE FOI MAIOR QUE O NUMERO SECRETO!")
            elif(menor):
                print("VOCE ERROU, O SEU CHUTE FOI MENOR QUE O NUMERO SECRETO!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(rodada == total_de_rodadas):
                print("VOCÊ NÃO CONSEGUIU ACERTAR O NUMERO SECRETO {} E SUA PONTUAÇÃO FINAL FOI DE {} PONTOS". format(numero_secreto, pontos))

    print("FIM DE JOGO")