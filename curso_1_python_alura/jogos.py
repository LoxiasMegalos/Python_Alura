import aula_7_alura
import aula_8_alura

#Alura_aula_7_curso_1_Python
#Números aleatorios - Random

print("*******************************************", end="\n")
print("ESCOLHA O SEU JOGO*************************")
print("*******************************************")

print("(1) FORCA (2) advinhacao")

jogo = int(input("Qual o jogo?: "))

if(jogo == 1):
    print("JOGANDO FORCA")
    aula_8_alura.jogar()
elif(jogo == 2):
    print("JOGANDO ADVINHACAO")
    aula_7_alura.jogar()

