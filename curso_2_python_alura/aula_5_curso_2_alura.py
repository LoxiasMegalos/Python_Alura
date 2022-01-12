#AULA 5 CURSO 2 PYTHON ALURA

def forca():
    print("JOGANDO FORCA!")

    palavra_secreta = "fruta do conde".upper()
    letras_acertadas = ["_" if letra != " " else " " for letra in palavra_secreta]

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

            if(limite-erros != 0):
                print("Você ainda tem {} tentativas antes morrer".format(limite-erros))


        #enforcou = erros == limite
        #acertou = "_" not in letras_acertadas


        if(letras_acertadas.count("_") == 0 or erros == limite):
            break
        print(letras_acertadas)

            #acertou = True
    if(acertou):
        print("PARABENS! VOCÊ GANHOU")
    else:
        print("PARABENS! VOCÊ PERDEU")

    print("Fim de Jogo!")



if(__name__ == "__main__"):
    forca()