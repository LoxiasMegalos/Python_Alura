#APLICANDO ORIENTAÇÃO A OBJETOS NO PROJETO:

#url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = " a "

#Sanitização da URL
#url = url.replace(" ", "")
url = url.strip()

#Validação da URL
if (url ==""):
    raise ValueError("A URL ESTÁ VAZIA!")

url_base = url[0 : url.find("?")]
url_parametros = url[url.find("?")+1:]

print(url_parametros)

parametro_procurado = "quantidade"

parametro_inicio = url_parametros.find(parametro_procurado)
tamanho_parametro = len(parametro_procurado)
inicio_valor = parametro_inicio + tamanho_parametro + 1
verifica_e_comercial = url_parametros.find("&", inicio_valor)

if(verifica_e_comercial == -1):
    print(url_parametros[inicio_valor:])
else:
    print(url_parametros[inicio_valor:verifica_e_comercial])