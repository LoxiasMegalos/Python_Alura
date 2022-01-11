#TUPLAS

def forca():
    print("*************************************")
    print("*********JOGANDO FORCA***************")
    print("*************************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    acertou = False
    enforcou = False


    print(letras_acertadas)

    while(not acertou and not enforcou):
        chute = input("Digite uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = chute
            index = index + 1

        print(letras_acertadas)

        if(letras_acertadas.count("_") == 0):
            print("PARABENS!")
            acertou = True

    print("FIM DE JOGO!")

if(__name__ == "__main__"):
    forca()