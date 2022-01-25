# 25/01/2022 - String em Python: Extraindo informações de URLS
# Em [0:1] o primeiro argumento e´inclusivo e o segundo é exclusivo
url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

url_base = url[0:19]
print(url_base)

url_parametros = url[20:36]
print(url_parametros)

url ="https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
inicio = 0
final = len(url)
ponto = 0
base = ""
parametros = ""

for digito in url:

    if (digito == "?"):
        base = url[inicio:ponto]
        parametros = url[ponto+1 : final]
        break

    ponto += 1

print(base)
print(parametros)

nome_completo = "Luciano Saldanha"
primeiro_nome = nome_completo[0:7]
segundo_nome = nome_completo[8:16]

print(primeiro_nome)
print(segundo_nome)

x = "oi"
y = "oi"

print(id(x))
print(id(y))