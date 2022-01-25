
#EXTRAIR O VALOR DO PARÂMETRO CURSO:

url_mariana = "https://www.alura.com.br/curso?curso=python&espec=data_science"

url_base = url_mariana[0:url_mariana.find("?")]
url_parametros = url_mariana[url_mariana.find("?")+1:]

print("Os parâmetros da URL são: {}".format(url_parametros))

parametro_buscado = "curso"
print("Buscamos o valor do parametro: {}".format(parametro_buscado))
parametro_inicio = url_parametros.find(parametro_buscado)
tamanho_parametro = len(parametro_buscado)
inicio_valor = parametro_inicio + tamanho_parametro + 1
parametro_e_comercial = url_parametros.find("&", inicio_valor)

if(parametro_e_comercial != -1):
    print("O valor é: {}".format(url_parametros[inicio_valor: parametro_e_comercial]))
else:
    print("O valor é: {}".format(url_parametros[inicio_valor:]))