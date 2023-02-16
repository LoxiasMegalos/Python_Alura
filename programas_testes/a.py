

def a():
    def soma(a,b):
        c= a+b
        return c



    inta = 2
    intb = 3
    #intc = soma(inta,intb)
    print("A soma de %d e %d é:" %(inta, intb), soma(inta,intb))

    print ("OiMundo.x")

#if (__name__ == "__main__"):
#    a()



v = ["11 + 11"]
#print(len(v))
operacao = " "


for i in range(len(v)):
    y = ""
    for x in v[i]:
        if x !="+" or x != "-":
            y += x
        elif x == "+" or x == "-":
            operacao = x
            y = y.strip()
            a = int(y)
            y = " "
    print(a)
    print(operacao)
    y = y.strip()
    b = int(y)
    #separador = 1 + len(operacao + str(b))
    if(operacao == "+"):
        resultado = a + b
        print("{} \n {} {} \n {} \n {}".format(a, operacao, b, "-"*5, resultado))
    if(operacao == "-"):
        resultado = a - b
        print("{} \n {} {} \n {} \n {}".format(a, operacao, b, "-"*5, resultado))




