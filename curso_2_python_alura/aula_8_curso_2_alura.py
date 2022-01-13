#JOGO FORCA DEFINITIVO ALURA

import Funcoes

def jogar ():

    Funcoes.imprime_mensagem_abertura()
    palavra_secreta = Funcoes.carrega_palavra_secreta("palavras.txt", 1)

    letras_acertadas = Funcoes.inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    acertou = False
    enforcou = False
    limite = len(palavra_secreta)
    erros = 0

    while(not acertou and not enforcou):

        chute = Funcoes.pede_chute()

        if(chute in palavra_secreta):
            letras_acertadas = Funcoes.marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            Funcoes.desenha_forca(erros)
            Funcoes.verifica_erros(chute, erros)

        acertou = "_" not in letras_acertadas
        enforcou = erros == 7

        print(letras_acertadas)

    Funcoes.imprime_mensagem_resultado(acertou, palavra_secreta)

if(__name__ == "__main__"):
    jogar()