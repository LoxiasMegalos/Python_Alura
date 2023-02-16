

'''
vetor_input = []
tamanho = int(input("Insira o tamanho do vetor: "))
for i in range(0, tamanho):
    vetor_input.append(int(input("Digite o {}º valor: ".format(i))))

print(vetor_input)
'''
vetor = [10,20,30,1,2]
primeira_seq = 0
quantidade_de_elementos = 0
quantidade_de_elem_2_seq = 0
index = 0

for i in range(len(vetor)):

    if vetor[i+1] > vetor[i] and i+1 <= len(vetor) and primeira_seq == 0:
        posicao_inicio = i
        quantidade_de_elementos += 1
        j = i
        z = i

    elif vetor[i+1] > vetor[i] and i+1 <= len(vetor) and primeira_seq != 0:
        inicio_seg_seq = i
        quantidade_de_elem_2_seq = 1
        z = i

    while(vetor[j+1] > vetor[j] and primeira_seq == 0):
        quantidade_de_elementos += 1
        j += 1

    while (vetor[z+1] > vetor[z] and primeira_seq == 1 and z+1 <= len(vetor)):
        quantidade_de_elementos += 1
        z += 1

    if(primeira_seq == 0 and quantidade_de_elementos > 0):
        primeira_seq = 1
        i = j
    elif (primeira_seq != 0 and quantidade_de_elem_2_seq > 0):
        i = z

    if(quantidade_de_elementos <= quantidade_de_elem_2_seq):
        posicao_inicio = inicio_seg_seq
        quantidade_de_elementos = quantidade_de_elem_2_seq




print(vetor[posicao_inicio:posicao_inicio+quantidade_de_elementos])