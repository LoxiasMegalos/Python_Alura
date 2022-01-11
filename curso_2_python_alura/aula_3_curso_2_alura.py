# AULA 3 CURSO 2 DE PYTHON ALURA - TRABALHANDO COM LISTAS

def forca():

    print("***********************************")
    print("*****JOGANDO FORCA*****************")
    print("***********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_","_","_","_","_"]
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual é a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encotrei a letra {1} na posição {2} da palavra {0}".format(palavra_secreta, chute, index))
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

        x = 0
        for letra in letras_acertadas:
            if(letra == "_"):
                x = x + 1
        if (x > 1):
            print("Ainda faltam {} letras para serem descobertas".format(x))
        if(x == 1):
            print("Ainda falta {} letra para serem descobertas".format(x))
        if(x == 0):
            print("PARABENS!")
            acertou = True


    print("Fim de Jogo!")

if(__name__ == "__main__"):
    forca()