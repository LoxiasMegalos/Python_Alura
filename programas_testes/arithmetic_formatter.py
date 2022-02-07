string = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "0 + 0", "15 + 12", "15 + 11", "15 + 2"]
lista_cima = []
lista_meio = []
lista_sep = []
lista_resultado = []
for termo in range(len(string)):
    y = ""
    for elemento in string[termo]:

        if elemento == "-" or elemento == "+" :
            y = y.strip()
            a = int(y)
            operacao = elemento
            y = ""

        y += elemento

    if y.startswith("+"):
        y = y[1:]
    elif y.startswith("-"):
        y = y[1:]

    y = y.strip()
    b = int(y)
    if operacao == "+":
        resultado = a + b
    elif operacao == "-":
        resultado = a - b
    if a > b:
        espacos = len(str(a)) + 2
    else:
        espacos = len(str(b)+operacao) + 1

    n = espacos - len(str(a))
    cima = n*" "+ str(a)
    n = espacos - len(str(b)+operacao)
    meio = operacao + n*" "+str(b)
    baixo = espacos*"-"
    n = espacos - len(str(resultado))
    s_resultado = n*" "+ str(resultado)
    lista_cima.append(cima)
    lista_meio.append(meio)
    lista_sep.append(baixo)
    lista_resultado.append(s_resultado)

print(*lista_cima, sep="    ")
print(*lista_meio, sep="    ")
print(*lista_sep, sep="    ")
print(*lista_resultado, sep="    ")




