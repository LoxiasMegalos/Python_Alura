import re

print("Este é o primeiro programa do segundo curso de Python da Alura - avançando na linguagem")

def forca():
    print("**********************************************")
    print("**********BEM VINDO AO JOGO DA FORCA**********")
    print("**********************************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    #enquanto (True)
    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        if(re.search(chute, palavra_secreta)):
            print("Voce acertou")
            enforcou = True
            acertou = True
        else:
            print("Voce errou")


        #print("Jogando")


    print("Fim de Jogo! Obrigado por jogar!")


if(__name__ == "__main__"):
    forca()
