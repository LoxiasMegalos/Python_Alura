#AULA 1 - LAÇO WHILE e operador not para inverter um valor bool
#AULA 2 - Laços com strings e funções built ins

#find

palavra = "aluracursos"
print(palavra.find("l"))
print(palavra.find("a"))
print(palavra.find("b"))

palavra = "terra"

index = 0
for letra in palavra:
    if(letra):
        print("A letra {} representa a posição {} da string".format(letra,index))
    index = index + 1

print()
palavra = "Alura"
ref = 0
for artel in palavra:
    if("l" == artel):
        print("Achou a letra {} na posição {}".format(artel, ref))
    ref = ref + 1

a = "cavalo"
b = "baleia"
print()
print("{1} e {0}".format(a,b))
print()

palavra = "testando_tudo"
print(palavra.endswith("do"))
print(palavra.startswith("tes"))
print(palavra.capitalize())
print(palavra.upper())
print(palavra.lower())
print()