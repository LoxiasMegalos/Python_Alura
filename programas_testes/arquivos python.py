
import random
banana = []

arquivo = open("batata.txt", "r")

for linha in arquivo:
    banana.append(linha.upper().strip())

arquivo.close()

print(banana)

relogio = [ "*" for fruta in banana]
print(relogio)

oculos = ["*" for fruta in banana if fruta == "MORANGO" ]
print(oculos)

celular = ["te amo" if fruta == "MORANGO" else "*" for fruta in banana]
print(celular)

random.seed(1)
numero = random.randrange(0, len(banana))
palavra = banana[numero]
print(palavra)


v = []
for letra in palavra:
    v.append(letra.lower())
print(v)