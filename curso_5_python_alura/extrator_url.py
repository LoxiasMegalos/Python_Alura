import re
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
        verifica_começo_base = self.get_url_base().startswith("https://")
        if not (self.url):
            print("Objeto não criado")
            raise ValueError("A URL ESTÁ VAZIA!")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        url_base = self.url[0 : self.url.find("?")]
        return url_base

    def get_url_parametros(self):
        url_parametros = self.url[self.url.find("?")+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_procurado):
        parametro_inicio = self.get_url_parametros().find(parametro_procurado)
        inicio_valor = parametro_inicio + len(parametro_procurado) + 1
        verifica_e_comercial = self.get_url_parametros().find("&", inicio_valor)
        if (verifica_e_comercial == -1):
            valor = self.get_url_parametros()[inicio_valor:]
        else:
            valor = self.get_url_parametros()[inicio_valor:verifica_e_comercial]
        return valor

    def conversao(self, valor,):
        O = self.get_valor_parametro("moedaOrigem")
        D = self.get_valor_parametro("moedaDestino")
        quantidade = int(valor)
        valor_dolar = 5.50
        if(quantidade == 0 or quantidade < 0):
            raise ValueError("A quantidade não pode estar vazia ou ser negativa!")
        elif(O == "dolar" and D == "real"):
            conversao = quantidade * valor_dolar
            return "O: {}, D:{}, Q:{}, Você terá {} R$".format(self.get_valor_parametro("moedaOrigem"), self.get_valor_parametro("moedaDestino"), self.get_valor_parametro("quantidade"), conversao)
        elif (O == "real" and D == "dolar"):
            conversao = quantidade / valor_dolar
            return "O: {}, D:{}, Q:{}, Você terá {} Dólares".format(self.get_valor_parametro("moedaOrigem"),self.get_valor_parametro("moedaDestino"),self.get_valor_parametro("quantidade"), conversao)

extrator_url = ExtratorURL("https://www.bytebank.com.br/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=11")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
print(extrator_url.conversao(11))


def foo(valor):
    if(valor):
        print("Valor é Verdadeiro")
    else:
        print("Valor é Falso")


