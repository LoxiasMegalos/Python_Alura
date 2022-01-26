#EXPRESSÕES REGULARES:

class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        print("Objeto criado em {}".format(self))

    def sanitiza_url(self, url):
        if (type(url) == str):
            return url.strip()
        else:
            return ""

    def valida_url(self):
        print(self.get_base())
        if not(self.url):
            print("Objeto não criado")
            raise ValueError("A URL não é válida")
        elif not(self.get_base().startswith("https://")):
            print("Objeto não criado")
            raise ValueError("A URL não inicia com https://")
        elif not(self.get_base().endswith("/cambio")):
            print("Objeto não criado")
            raise ValueError("Você não pode tentar acessar o cambio em uma pagina sem /cambio")

    def get_base(self):
        url_base = self.url[0:self.url.find("?")]
        return url_base

    def get_parametros(self):
        url_parametros = self.url[self.url.find("?")+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_procurado):
        inicio_parametro = self.get_parametros().find(parametro_procurado)
        inicio_valor = inicio_parametro + len(parametro_procurado) + 1 #=
        verifica_e_comercial = self.get_parametros().find("&", inicio_valor)

        if(verifica_e_comercial == -1):
            valor = self.get_parametros()[inicio_valor:]
        else:
            valor = self.get_parametros()[inicio_valor:verifica_e_comercial]

        if(parametro_procurado == "quantidade"):
            return self.valida_quantidade(valor)
        else:
            return valor


    def valida_quantidade(self, valor):
        valor = int(valor)
        if (valor == 0 or valor < 0):
            raise ValueError("A quantidade de moedas para serem convertidas não pode ser 0 ou inferior a isso!")
        else:
            return valor

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