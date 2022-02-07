from validate_docbr import CPF, CNPJ
import re
from datetime import datetime, timedelta

horas = datetime.today()
print(horas.strftime("%d,%m,%Y %H:%M"))

padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
telefone = "5511943220607"
verifica = re.search(padrao, telefone)
print(verifica.group(1))

#DOCUMENTOS - FACTORY E INSTANCIAÇÃO DE CLASSES - BIBLIOTECA DO PYPI

class CriaDoc:

    @staticmethod
    def verifica(documento):
        documento = str(documento)
        if(len(documento) == 11):
            return DocCpf(documento)
        elif(len(documento) == 14):
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de Dígitos Inválida")

class DocCpf:

    def __init__(self, documento):
        if(self.verifica(documento)):
            self.cpf = documento
        else:
            raise ValueError("CPF INVÁLIDO!")

    def __str__(self):
        return self.mascara()

    def verifica(self, cpf):
        validator = CPF()
        teste = validator.validate(cpf)
        if(teste):
            return True
        else:
            return False

    def mascara(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:

    def __init__(self, documento):
        if(self.verifica(documento)):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ INVALIDO!")

    def __str__(self):
        return self.mascara()

    def verifica(self, cnpj):
        validador = CNPJ()
        teste = validador.validate(cnpj)
        if(teste):
            return True
        else:
            return False

    def mascara(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


murillo = CriaDoc.verifica(48988752899)
mokka = CriaDoc.verifica(21220932000110)

print(murillo)
print(mokka)

#TELEFONES - VALIDANDO E IMPRIMINDO NO PADRAO BR

class Telefone:

    def __init__(self, numero):
        numero = str(numero)
        if(self.verifica(numero)):
            self.numero = numero
        else:
            raise ValueError("TELEFONE NO PADRÃO INCORRETO")

    def __str__(self):
        return self.formata_numero()

    def verifica(self, numero):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        teste = re.findall(padrao, numero)
        if(teste):
            return True
        else:
            return False

    def formata_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
        numero = re.search(padrao, self.numero)
        formatacao = "+{}({}){}-{}".format(numero.group(1),numero.group(2),numero.group(3),numero.group(4))
        return formatacao

cellmurillo = Telefone(5511943220607)
print(cellmurillo)

class Datas:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def formata_data(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def verifica_mes(self):
        meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]
        mes_cadastro = self.momento_cadastro.month
        return meses[mes_cadastro - 1]

    def verifica_dia(self):
        dias = ["seg","ter","quar","quin","sex","sab","dom"]
        dia_cadastro = self.momento_cadastro.weekday()
        return dias[dia_cadastro]

    def verifica_tempo(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro

cadastro = Datas()
print(cadastro)
print(cadastro.verifica_mes())
print(cadastro.verifica_dia())
print(cadastro.verifica_tempo())

#CEP

