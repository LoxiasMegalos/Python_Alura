

def selecionar(nivel):
    x = 0
    print("Selecione o nível de dificuldade: ")
    print("(1) FÁCIL (2) MÉDIO (3) DIFÍCIL ")
    while (x != 1):
        nivel = int(input("Defina o nivel: "))
        if (nivel == 1 or nivel == 2 or nivel == 3):
            x = 1
        else:
            print("SELECIONE UM NIVEL DE DIFICULDADE VALIDO!")
    if (nivel == 1):
        return 20
    elif (nivel == 2):
        return 10
    else:
        return 5

def chute_numero(rodada):
    chute = input("Digite um numero:")
    return chute

def comparacao_igual(chute,numero_secreto):
    acertou = chute == numero_secreto
    return acertou

def comparacao_maior(chute,numero_secreto):
    acertou = chute > numero_secreto
    return acertou

def comparacao_menor(chute,numero_secreto):
    acertou = chute < numero_secreto
    return acertou

def verificacao(rodada, total_de_rodadas, pontos, igual, maior, menor, numero_secreto):
    if(igual):
        print("Voce acertou o numero secreto e fez {} pontos".format(pontos))
    else:
        if(maior and rodada != total_de_rodadas):
            print("Você errou o numero secreto, seu chute foi maior")
        elif(menor and rodada != total_de_rodadas):
            print("Você errou o numero secreto, seu chute foi menor")
        elif(maior and rodada == total_de_rodadas):
            print("Voce não acertou o numero secreto {}, e sua pontuaçao final foi de {} pontos".format(numero_secreto, pontos))
        elif (menor and rodada == total_de_rodadas):
            print("Voce não acertou o numero secreto {}, e sua pontuaçao final foi de {} pontos".format(numero_secreto, pontos))