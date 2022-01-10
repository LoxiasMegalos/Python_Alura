import re

def forca():
    print("*****************************************")
    print("******JOGO DA FORCA**********************")
    print("*****************************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        #chute = chute.lower()
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute, index))
            index = index + 1


        print("jogando...")

    print("Obrigado por Jogar")

if (__name__=="__main__"):
    forca()