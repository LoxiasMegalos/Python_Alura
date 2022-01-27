import random

#ULTIMA AULA CURSO 2 ALURA

def jogar():

    print("JOGANDO FORCA!")

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip().upper())

    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero]

    letras_acertadas = ["_" if letra in palavra_secreta != " " else " " for letra in palavra_secreta]

    acertou = False
    enforcou = False

    limite = len(palavra_secreta)
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = chute
                index += 1

        else:
            erros += 1
            print("Você errou, ainda faltam {} antes de ser enforcado".format(limite-erros))

        acertou = "_" not in letras_acertadas
        enforcou = erros == limite

        print(letras_acertadas)

    if(acertou):
        print("Você acertou a palavra secreta {} e ainda restaram {} tentativas".format(palavra_secreta, limite - erros))
    else:
        print("Você errou e enforcou :(")

    print("FIM DE JOGO!")

if(__name__ == "__main__"):
    jogar()