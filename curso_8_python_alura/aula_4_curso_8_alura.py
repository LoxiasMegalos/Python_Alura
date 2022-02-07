from validate_docbr import CPF, CNPJ
import re

#tel = "5511943220607"
#p = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#res = re.search(p, tel)
#print(res.group(1))


class CriaDocumento:

    @staticmethod
    def valida_documento(documento):
        documento = str(documento)
        if(len(documento)==11):
            return DocCpf(documento)
        elif(len(documento)==14):
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de Dígitos Inválida!")


class DocCpf:

    def __init__(self, documento):
        self.cpf = self.valida_cpf(documento)

    def valida_cpf(self, cpf):
        validador = CPF()
        if validador.validate(cpf):
            return cpf
        else:
            raise ValueError("CPF INVÁLIDO!")

    def __str__(self):
        return self.mascara_cpf()

    def mascara_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:

    def __init__(self, documento):
        self.cnpj = self.valida_cnpj(documento)

    def valida_cnpj(self, cnpj):
        validador = CNPJ()
        if validador.validate(cnpj):
            return cnpj
        else:
            raise ValueError("CNPJ INVÁLIDO!")

    def __str__(self):
        return self.mascara_cnpj()

    def mascara_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


class CriaTelefone:

    def __init__(self, numero):

        if(self.valida_telefone(numero)):
            self.numero = numero
        else:
            raise ValueError("Numero Invalido!")

    def valida_telefone(self, numero):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        verifica = re.findall(padrao, numero)
        if verifica:
            return True
        else:
            return False

    def __str__(self):
        return self.mascara_telefone()

    def mascara_telefone(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
        grupo = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(grupo.group(1), grupo.group(2), grupo.group(3), grupo. group(4))
        return numero_formatado




telefone = "5511943220607"

teste_class = CriaTelefone(telefone)
print(teste_class)

teste_cpf = CriaDocumento.valida_documento(48988752899)
teste_cnpj = CriaDocumento.valida_documento(21220932000110)
print(teste_cpf)
print(teste_cnpj)
