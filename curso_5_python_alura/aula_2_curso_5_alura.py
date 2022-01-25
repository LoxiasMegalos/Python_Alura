#UTILIZANDO MÉTODOS DE STRINGS

url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url_encurtada = "bytebank.com/cambio?moedaOrigem=real"

indice_interrogacao = url.find("?")
indice_interrogacao_curto = url_encurtada.find("?")
indice_final = len(url)

#SEPARA A BASE DA URL DOS PARAMETROS
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+ 1:]
print(url_base)
print(url_parametros)

#BUSCA O VALOR DE UM PARAMETRO

parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
tamanho_parametro = len(parametro_busca)
indice_valor = indice_parametro + tamanho_parametro + 1
indice_e_comercial = url_parametros.find("&", indice_valor)

if (indice_e_comercial == -1):
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor : indice_e_comercial]

print(valor)