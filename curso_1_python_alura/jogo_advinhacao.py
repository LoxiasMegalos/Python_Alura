# Jogo Advinhacao Alura
import Nivel

def adv():
    import random

    print("*******************************")
    print("Bem vindo ao jogo da advinhacao")
    print("*******************************")

    nivel = 0
    total_de_rodadas = Nivel.selecionar(nivel)
    numero_secreto = random.randrange(1, 101)
    pontos = 1000
    #print(numero_secreto)

    for rodada in range(1, total_de_rodadas + 1):
        print("Rodada {} de {}".format(rodada, total_de_rodadas))


        chute = Nivel.chute_numero(rodada)
        chute = int(chute)
        if(chute < 1 or chute > 100):
            print("Voce Deve digitar um numero entre 1 e 100! Perdeu uma rodada")
            continue

        acertou = Nivel.comparacao_igual(chute, numero_secreto)
        maior = Nivel.comparacao_maior(chute, numero_secreto)
        menor = Nivel.comparacao_menor(chute, numero_secreto)

        pontos_rodada = abs(numero_secreto - chute)
        pontos = pontos - pontos_rodada

        Nivel.verificacao(rodada, total_de_rodadas, pontos, acertou, maior, menor, numero_secreto)

        if(acertou):
            break

    print("FIM DE JOGO")

if(__name__ == "__main__"):
    adv()