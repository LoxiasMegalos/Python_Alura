
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

#EXPRESSÕES REGULARES, BIBLIOTECA re - re.compile(padrão) - search - group | [], {}, ?

import re

#CEP - 5 dígitos + hifen (opcional) + 3 dígitos
endereco = "Rua das Flores 72, apartamento 10002, RS,Lanrajeiras, Rio de Janeiro, 09230-590"

padraocep = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padraocep.search(endereco) #Match

padraoestado = re.compile("[A-Z]{2}")
buscaestado = padraoestado.search(endereco)

if busca:
    cep = busca.group()
    print(cep)

if buscaestado:
    uf = buscaestado.group()
    print(uf)

#CPF

cpf_rafa = "Rafaela Brasil, CPF: 718.457.190-85"
padraocpf = re.compile("[0-9]{3}[.]{1}[0-9]{3}[.]{1}[0-9]{3}[-]{1}[0-9]{2}")

buscacpf = padraocpf.search(cpf_rafa)

if buscacpf:
    cpf = buscacpf.group()
    print(cpf)

#SITE

url = "https://www.mokka-sensors.com.br/encoders"
padrao_url = re.compile("(http(s)?://)?(www.)?mokka-sensors.com(.br)?/encoders")
match = padrao_url.match(url)

if not match:
    raise ValueError("URL Invalida")

print("URL valida!")

#VERIFICANDO MÉTODOS EM OBJETOS:

print(dir(str))
print('__len__' in dir(str))
print(dir(float))

#identidades

x = "abc"
y = "abc"
print(id(x))
print(id(y))

print(x == y)
print( x is y)
print(bool("") is False)