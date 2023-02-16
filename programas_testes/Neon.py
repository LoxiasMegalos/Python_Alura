
numero = 1
n = 7
v = []

for n in range(0,n):
    if(n < 2):
        x = 1
        v.append(1)
        #print(x)
        continue
    n_menos1 = v[n-1]
    n_menos2 = v[n-2]
    atual = n_menos1 + n_menos2
    v.append(atual)
    #print(v[n])

print(v)



frase = "diversao"
frasenova = frase.replace(" ","").upper()
print(frasenova)

if(len(frasenova)/2 < 1):
    print("1 - palavra de letra unica palindromo")
    SystemExit

index = len(frasenova)-1
posicoes_verificadas = int(len(frasenova)/2)
acertos = 0
vezes_verificadas = 0

for letra in frasenova:
    vezes_verificadas += 1
    if(vezes_verificadas > posicoes_verificadas):
        break
    verifica = (letra == frasenova[index])
    if(verifica):
        acertos += 1
    index -= 1

if(acertos == posicoes_verificadas):
    print("1 - palindromo")
else:
    print("0 - nao eh palindromo")