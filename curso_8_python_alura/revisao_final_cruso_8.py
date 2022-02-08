from validate_docbr import CNPJ, CPF
from datetime import datetime, timedelta
import re
import requests

class Documento:

    @staticmethod
    def verifica_doc(documento):
        documento = str(documento)
        if(len(documento)==11):
            return DocCpf(documento)
        elif(len(documento)==14):
            return DocCnpj(documento)
        else:
            raise ValueError("Documento Inválido!!!")

class DocCpf:

    def __init__(self, documento):
        if(self.verifica(documento)):
            self.cpf = documento
        else:
            raise ValueError("CPF INVÁLIDO!")

    def __str__(self):
        return self.formata(self.cpf)

    def verifica(self, documento):
        validador = CPF()
        if(validador.validate(documento)):
            return True
        else:
            return False

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:

    def __init__(self, documento):
        if(self.verifica(documento)):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ INVÁLIDO!")

    def __str__(self):
        return self.formata(self.cnpj)

    def verifica(self, documento):
        validador = CNPJ()
        if(validador.validate(documento)):
            return True
        else:
            return False

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

class Telefone:

    def __init__(self, telefone):
        if(self.verifica(telefone)):
            self.tel = telefone
        else:
            raise ValueError("Numero Inválido!")

    def __str__(self):
        return self.formata(self.tel)

    def verifica(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
        if(re.findall(padrao,telefone)):
            return True
        else:
            return False

    def formata(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
        grupos = re.search(padrao, self.tel)
        return "+{}({}){}-{}".format(grupos.group(1),grupos.group(2),grupos.group(3),grupos.group(4))

class Data:

    def __init__(self):
        self.novo_cliente = datetime.today()

    def __str__(self):
        return self.data_cadastro()

    def data_cadastro(self):
        return self.novo_cliente.strftime("%d/%m/%Y %H:%M")

    def mes_cadastro(self):
        meses = ["jan","fev","mar","abr","mai","jun","jul","ago","sep","out","nov","dez"]
        mes_cadastro = self.novo_cliente.month
        return meses[mes_cadastro - 1]

    def dia_cadastro(self):
        dias = ["seg","ter","quar","quin","sex","sab","dom"]
        dia_cadastro = self.novo_cliente.weekday()
        return dia_cadastro,dias[dia_cadastro]

    def tempo_cadastro(self):
        return (datetime.today() + timedelta(days=30)) - self.novo_cliente

#25230590
class Cep:

    def __init__(self, cep):
        cep = str(cep)
        if(self.verifica(cep)):
            self.cep = cep
        else:
            raise ValueError("CEP INVÁLIDO")

    def __str__(self):
        return self.formata()

    def verifica(self, cep):
        if(len(cep) == 8):
            return True
        else:
            return False

    def formata(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def endereco(self):
        #url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        #dados2 = r.text - lista de uma API
        return "Logradouro: {} | Bairro: {} | UF: {} | CEP: {}".format(dados["logradouro"],dados["bairro"], dados["uf"], dados["cep"])


#murillo = Data()
#print(murillo)
#print(murillo.mes_cadastro())
#print(murillo.dia_cadastro())
#print(murillo.tempo_cadastro())
#cep = Cep(25230590)
#print(cep)

murillo = Cep("09230590")
print(murillo.endereco())