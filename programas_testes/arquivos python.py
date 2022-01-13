
banana = []

arquivo = open("../curso_2_python_alura/batata.txt", "r")

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