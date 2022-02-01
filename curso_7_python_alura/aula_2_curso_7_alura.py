numeros_pares = [0,2,4,6,8]
numeros = [0,1,2,3,4,5,6,7,8,9]
numeros_impares = [1,3,5,7,9]

np_set = set(numeros_pares)
ni_set = set(numeros_impares)
n_set = set(numeros)

print(n_set)

print(np_set | ni_set)
print(np_set & ni_set)
print(np_set - ni_set)
print(n_set - ni_set)
print(5 in np_set)
print(6 in np_set)
print(np_set ^ n_set)

#FINALIZANDO O TRABALHO INICIAL COM CONJUNTOS

print("Modificando conjunto:")

usuarios = {1 , 10, 17, 19 , 20}
print(len(usuarios))
usuarios.add(17)
print(len(usuarios))
usuarios.add(18)
print(len(usuarios))
print(type(usuarios))
usuarios = frozenset(usuarios)
print(type(usuarios))

#CONJUNTO COM TEXTOS:

texto_set = "Bem vindo meu nome é Murillo eu gosto muito de nomes e tenho o meu cachorro e gosto muito de carro"
print(texto_set.split())
texto = set(texto_set.split())
print(texto)