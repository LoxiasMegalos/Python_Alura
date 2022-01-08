# Jogo Forca Alura

def forca():
    import random

    print("*******************************")
    print("Bem vindo ao jogo da advinhacao")
    print("*******************************")

    def selecionar_nivel(a):
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

    def comparacao_igual(chute, numero_secreto):
        acertou = chute == numero_secreto
        return acertou

    def comparacao_maior(chute, numero_secreto):
        acertou = chute > numero_secreto
        return acertou

    def comparacao_menor(chute, numero_secreto):
        acertou = chute < numero_secreto
        return acertou

    def verificacao(rodada, total_de_rodadas, pontos, igual, maior, menor, numero_secreto):
        if (igual):
            print("Voce acertou o numero secreto e fez {} pontos".format(pontos))
        else:
            if (maior and rodada != total_de_rodadas):
                print("Você errou o numero secreto, seu chute foi maior")
            elif (menor and rodada != total_de_rodadas):
                print("Você errou o numero secreto, seu chute foi menor")
            elif (maior and rodada == total_de_rodadas):
                print("Voce não acertou o numero secreto {}, e sua pontuaçao final foi de {} pontos".format(
                    numero_secreto, pontos))
            elif (menor and rodada == total_de_rodadas):
                print("Voce não acertou o numero secreto {}, e sua pontuaçao final foi de {} pontos".format(
                    numero_secreto, pontos))

    nivel = 0
    total_de_rodadas = selecionar_nivel(nivel)
    numero_secreto = random.randrange(1, 101)
    pontos = 1000
    print(numero_secreto)

    for rodada in range(1, total_de_rodadas + 1):
        print("Rodada {} de {}".format(rodada, total_de_rodadas))

        chute = chute_numero(rodada)
        chute = int(chute)
        if (chute < 1 or chute > 100):
            print("Voce Deve digitar um numero entre 1 e 100!")
            continue

        acertou = comparacao_igual(chute, numero_secreto)
        maior = comparacao_maior(chute, numero_secreto)
        menor = comparacao_menor(chute, numero_secreto)

        pontos_rodada = abs(numero_secreto - chute)
        pontos = pontos - pontos_rodada

        verificacao(rodada, total_de_rodadas, pontos, acertou, maior, menor, numero_secreto)

        if (acertou):
            break

    print("FIM DE JOGO")

if(__name__ == "__main__"):
    forca()

