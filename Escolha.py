import jogo_advinhacao
import forca

print("VAMOS JOGAR UM JOGO")

def escolhe_jogo():
    x = 0
    while ( x != 1):
        opcao = int(input("Selecione o jogo: (1) Advinhacao (2) Forca (3) Sair: "))
        if(opcao == 1):
            print("Você selecionou advinhcao!")
            jogo_advinhacao.adv()
        elif(opcao == 2):
            print("Você selecionou forca!")
            forca.forca()
        elif(opcao == 3):
            print("OBRIGADO!")
            x = 1
        else:
            print("Digite uma opcao valida")

if(__name__ == "__main__")
    escolhe_jogo()
