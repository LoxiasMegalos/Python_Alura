#PYTHON COLLECTIONS PARTE 1 - LISTAS E TUPLAS

#COLEÇÕES -> + DE 1 ELEMENTO

idade_1 = 39
idade_2 = 30
idade_3 = 27
print(idade_1)
print(idade_2)
print(idade_3)
idades = [39, 30, 27, 15] #Sequência de valores de acesso aleatório
print(type(idades))
print("O tamanho da lista é: ", len(idades))
print(idades)
print("O termo na posição 3 é: ", idades[3])
for idade in idades:
    print(idade)
idades.append(15)
print(idades)
idades.remove(30)
print(idades)
idades.append(15)
print(idades)
idades.remove(15)
print(idades)
idades.append(27)
idades.remove(27)
print(idades)
idades.clear()
print(idades)

#MAIS OPERAÇÕES EM LISTAS E LIST COMPREHENSION
idades = [39, 30, 27, 15]
print("Está dentro?", 28 in idades)
print(15 in idades)

if 15 in idades:
    idades.remove(15)

if 28 in idades:
    idades.remove(28)

print(idades)

idades.insert(0,20)
print(idades)
idades.extend([24,19])
print(idades)

idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade+1)

print(idades_no_ano_que_vem)

#LIST COMPREHENSION

idades_no_ano_que_vem = [(idade + 1) for idade in idades]
print(idades_no_ano_que_vem)

print(idades)

idades = [idade for idade in idades if idade > 25]

print(idades)

#PROBLEMAS DA MUTABILIDADE DA LISTA

def faz_processamento_de_visualização(lista = []):
    print(len(lista))
    lista.append(13)

idades = [16,21,29,56,43]
faz_processamento_de_visualização()
faz_processamento_de_visualização()
faz_processamento_de_visualização()
faz_processamento_de_visualização()