#Alura_aula_2_curso_1_Python
#print("Este programa é a aula 2 do curso 1 de Python da ALURA", end="\n")
print("*******************************************", end="\n")
print("Bem vindo ao jogo de adivinhação!", end="\n")
print("*******************************************")

numero_secreto = 42

# chute = int(input("Digite o seu numero: "))
# ou
chute_str = input("Digite o seu numero: ")

chute = int(chute_str)

print("Você digitou ", chute)

if(chute == numero_secreto):
    print("Você acertou o número secreto")                           #identação de 4 espaços para reconhecer o bloco
else:
    print("O número secreto era:", numero_secreto,", mas você digitou:",chute)

print("Fim do jogo")
