#AULA 5 CURSO 2 PYTHON ALURA

def forca():
    print("JOGANDO FORCA!")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]
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
            print("Você ainda tem {} tentativas antes morrer".format(limite-erros))
        print(letras_acertadas)

        #enforcou = erros == limite
        #acertou = "_" not in letras_acertadas


        if(letras_acertadas.count("_") == 0 or erros == limite):
            break
            #acertou = True
    if(acertou):
        print("PARABENS! VOCÊ GANHOU")
    else:
        print("PARABENS! VOCÊ PERDEU")

    print("Fim de Jogo!")



if(__name__ == "__main__"):
    forca()