#Alura_aula_3_curso_1_Python
print("*******************************************", end="\n")
print("Bem vindo ao jogo de adivinhação!", end="\n")
print("*******************************************")

numero_secreto = 18

chute_str = input("Digite o número secreto: ")

chute = int(chute_str)

print("Você digitou:", chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

print("O tipo da variavel acertou é: ", type(acertou), end="\n")

if (acertou):
    print("Você acertou")
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto.")

print("FIM DE JOGO", end="\n")

# Se a condição satisfeita não for declarada no programa não vai haver nada na saída

usuario = "string"

teste_de_usuario = input("Digite uma string para ser comparada: ")

comparacao_string = usuario == teste_de_usuario

print(comparacao_string)

