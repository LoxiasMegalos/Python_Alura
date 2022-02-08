import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP INVALIDO!")

    def __str__(self):
        return self.format_cep()

    def cep_e_valido(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (dados["bairro"],
                dados["localidade"],
                dados["uf"])




#cep = BuscaEndereco("09230590")
#print(cep)
#bairro, cidade, uf = cep.acessa_via_cep()
#print(bairro, cidade, uf)

#print(cep.acessa_via_cep().text)
#print(cep.acessa_via_cep().json()["bairro"])
#print(type(cep.acessa_via_cep().text))
#print(type(cep.acessa_via_cep().json()))

#r = requests.get("https://viacep.com.br/ws/25230590/json/")
#print(r)
#print(r.text)
#print(type(r.text))