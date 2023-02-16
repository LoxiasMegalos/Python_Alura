b = '''
Implemente a função frequencia_string, que recebe uma string str e um texto. Por meio do parâmetro qtd (passado por referência), 
a função deve retornar a quantidade de vezes que str aparece no texto. Essa verificação deve ignorar diferenças em razão de letras minúsculas e maiúsculas. 
Por exemplo, considere str="teste" e texto="Teste teste TESTE". Nesse caso, a função deve retornar o valor 3.

'''

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

alfabeto_maiusculo = []

for letra in alfabeto:
    alfabeto_maiusculo.append(letra.upper())


str = "ABCA"
texto = "abcdeABCaBcAbcAbCABcabCaBCde"

valor = 0
ver = 0
count = 0
compara = 0
ver2 = 0


for letra in texto:

    for pinto in range(len(alfabeto)):
        if alfabeto[pinto] == letra or alfabeto_maiusculo[pinto] == letra:
            if str[0] == alfabeto[pinto] or str[0] == alfabeto_maiusculo[pinto]:
                ver += 1
                #print("{} é igual a {} em letra {} - index {}".format(letra, str[0], texto[count], count))
                break
    compara = count
    ver2 = ver
    while(ver >= 1 and ver < len(str)):
        count += 1
        for pinto in range(len(alfabeto)):
            if texto[count] == alfabeto_maiusculo[pinto] or texto[count] == alfabeto[pinto]:
                if str[ver] == alfabeto[pinto] or str[ver] == alfabeto_maiusculo[pinto]:
                    ver2 += 1
                    break
        if(texto[count] == " " and str[ver] == " "):
            ver2 += 1
        #print(str[ver])
        if(ver2 > ver):
            ver = ver2
            continue
        else:
            break

    if(ver == len(str)):
        valor += 1

    count = compara
    ver = 0
    count += 1

print(valor)