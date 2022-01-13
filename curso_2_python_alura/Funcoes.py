import random

def verifica_erros(chute, erros):
    if(7 - erros > 0):
        print("LETRA {} errada! Você ainda tem mais {} tentativas".format(chute, 7 - erros))

def marca_chute_correto(chute, palavra, letras):
    index = 0
    for letra in palavra:
        if (chute == letra):
            letras[index] = chute
        index += 1
    return letras

def imprime_mensagem_resultado(resultado, palavra):
    if (resultado):
        print("PARABENS")
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Você Perdeu")
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def imprime_mensagem_abertura():
    print("JOGANDO FORCA")

def carrega_palavra_secreta(arquivo_s, linha_inicial = 0):
    arquivo = open(arquivo_s, "r")

    palavras = []
    for linha in arquivo:
        palavras.append(linha.upper().strip())

    numero = random.randrange(linha_inicial, len(palavras))

    palavra_secreta = palavras[numero]

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" if letra != " " else " " for letra in palavra]

def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.upper().strip()
    return chute

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()