#CONJUNTOS E DICIONARIOS EM PYTHON

#SETS, DICIONARIOS, VARIAÇÕES, DEFAULT(DICT) E COUNTER
#MUITO UTILIZADAS NO DIA DIA
#CONTINUANDO COM COLLECTIONS

#Formas de agrupar elementos

#listas
usuarios_data_science = [15,23,43,56]
usuarios_machine_learning = [13,23,56,42]

#Colocar os alunos de data science e machine learning em uma nova lista com todas as listas
#copy - cópia rasa - referenciar
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)
print(len(assistiram))

#Há usuarios repetidos nas listas - pois as listas possuiam elementos em comum entre si
#Como ignorar os elementos repetidos? - Utilizando Conjuntos
print("Transformação de lista em conjunto")
print(set(assistiram))

conjunto_teste = {1,2,3,4,8,5,2,3,4}
print(conjunto_teste)
print(type(conjunto_teste))

set_criado = set(assistiram)
print(set_criado)
for usuario in set_criado:
    print(usuario)

lista_criada = list(set_criado)
print(lista_criada, end="\n\n\n")

print("OPERAÇÕES DE CONJUNTOS:")
print("Trabalhando com a UNIÃO DE 2 CONJUNTOS:")
usuarios_data_science = {15,23,43,56}
usuarios_machine_learning = {13,23,56,42}
print("OPERAÇÃO OU | :", usuarios_data_science | usuarios_machine_learning)
conjunto_ou = usuarios_data_science | usuarios_machine_learning
print("Trabalhando com a INTERSECÇÃO DE 2 CONJUNTOS:")
conjunto_e = usuarios_data_science & usuarios_machine_learning
print("OPERAÇÃO E & :", usuarios_data_science & usuarios_machine_learning)
print("Trabalhando com os elementos que não estão fora da intersecção DE 2 CONJUNTOS:")
conjunto_not = usuarios_data_science - usuarios_machine_learning
print("Os usuarios de um conjunto A que não estão em B são:", conjunto_not)
print("Verificando se um elemento está em um conjunto")
print("elemento in set", 15 in conjunto_not)
print("elemento in set", 30 in conjunto_not)
print("Ou exclusivo, fez um ou outro mas não os dois")
conjunto_xor = usuarios_data_science ^ usuarios_machine_learning
print("Os usuarios que fizeram ou um ou outro são", usuarios_data_science ^ usuarios_machine_learning)
