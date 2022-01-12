#AULA 6 CURSO 2 DE PYTHON ALURA
import random

def forca():
    print("JOGANDO FORCA!")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().upper())
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero]
    letras_acertadas = ["_" if letra != " " else " " for letra in palavra_secreta]

    print(letras_acertadas)

    acertou = False
    enforcou = False

    limite = len(palavra_secreta)
    tentativa = 0

    while(not acertou and not enforcou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()
        chute_p(chute,palavra_secreta,letras_acertadas)

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = chute
                index += 1

        else:
            tentativa += 1
            if (limite - tentativa != 0):
                print("Você ainda tem {} tentativas antes morrer".format(limite - tentativa))

        acertou = "_" not in letras_acertadas
        enforcou = tentativa == limite

        print(letras_acertadas)

    if(acertou):
        print("PARABENS!")
    else:
        print("Perdeu!")

    print("Fim de Jogo")



if(__name__ == "__main__"):
    forca()