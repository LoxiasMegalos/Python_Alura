#MÉTODOS ESPECIAIS - DUNDER METHODS

import re


class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def sanitiza_url(self, url):
        if not(type(url) == str):
            return ""
        else:
            return url.strip()

    def valida_url(self):

        if not (self.url):
            print("Objeto Não Criado!")
            raise ValueError("URL Invalida")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)

        if not match:
            print("Objeto Não Criado!")
            raise ValueError("URL Invalida")



    def get_base(self):
        base = self.url[0:self.url.find("?")]
        return base

    def get_parametros(self):
        parametros = self.url[self.url.find("?") + 1:]
        return parametros

    def get_valor_parametros(self, parametro_procurado):
        inicio_parametro = self.get_parametros().find(parametro_procurado)
        inicio_valor = inicio_parametro + len(parametro_procurado) + 1
        verifica_e_comercial = self.get_parametros().find("&",inicio_valor)

        if (verifica_e_comercial == -1):
            valor = self.get_parametros()[inicio_valor:]
        else:
            valor = self.get_parametros()[inicio_valor:verifica_e_comercial]
        if(parametro_procurado == "quantidade"):
            return self.valida_quantidade(valor)
        else:
            return valor

    def valida_quantidade(self, valor):
        valor = int(valor)
        if(valor == 0 or valor < 0):
            raise ValueError("Quantidade Inválida para a cconversão de moedas!")
        else:
            return valor

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_parametros() + "\n" + "URL Base: " + self.get_base()

    def __eq__(self, other):
        return self.url == other.url

url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=10"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print(id(extrator_url))
print(id(extrator_url_2))
print(extrator_url == extrator_url_2)
print("O tamanho da URL é: {}".format(len(extrator_url)))
print(extrator_url)
valor_quantidade = extrator_url.get_valor_parametros("quantidade")
print("Quantidade: {}".format(valor_quantidade))