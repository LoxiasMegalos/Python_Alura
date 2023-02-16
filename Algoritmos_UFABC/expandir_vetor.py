a = '''
Por exemplo, o vetor [10 10 10 10 10 50 50 10 10 10 90], após ser compactado, será [10 5 50 2 10 3 90 1].

Implemente a função expandir_vetor , que recebe um vetor compactado utilizando o método descrito anteriormente e então retorne um novo vetor com o resultado da expansão. Além disso, a função deve retornar a quantidade de elementos no vetor expandido por meio do parâmetro n_expandido (passado por referência).

Por exemplo, ao receber o vetor [10 5 50 2 10 3 90 1], o vetor expandido será [10 10 10 10 10 50 50 10 10 10 90].

'''

v = [10, 5, 50, 2, 10, 3, 90, 1]

nv = []
num = 0
vezes = 0

for numero in range(0,len(v)):
    if numero % 2 == 0:
        num = v[numero]
        continue
    vezes = v[numero]
    while(vezes != 0):
        nv.append(num)
        vezes -= 1

print(nv)
