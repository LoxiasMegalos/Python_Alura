a = 2
b = 0

soma = a + b
m = 1
x = 0
binario = ""

while(soma != 0 or soma != 1):
    if(m*2 > soma):
        soma = soma - m
        binario += "1"
        break
    m = m*2
print(m)
print(soma)

while(m != 1):
    m /= 2
    if(soma - m >= 0):
        binario += "1"
        soma = soma - m
    else:
        binario += "0"

print(binario)