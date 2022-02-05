from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def valida_documento(documento):
        documento = str(documento)
        if(len(documento)==11):
            return DocCpf(documento)
        elif(len(documento)==14):
            return DocCnpj(documento)
        else:
            raise ValueError("ERRO! QUANTIDADE DE DÍGITOS INVÁLIDA")


class DocCpf:

    def __init__(self, documento):
        self.cpf = self.valida_cpf(documento)

    def valida_cpf(self, documento):
        validador = CPF()
        if(validador.validate(documento)):
            return documento
        else:
            raise ValueError("CPF Inválido")

    def __str__(self):
        return self.formata_cpf()

    def formata_cpf(self):
        formatador = CPF()
        return formatador.mask(self.cpf)

class DocCnpj:

    def __init__(self, documento):
        self.cnpj = self.valida_cnpj(documento)

    def __str__(self):
        return self.formata_cnpj()

    def valida_cnpj(self, documento):
        validador = CNPJ()
        if(validador.validate(documento)):
            return documento
        else:
            raise ValueError("CNPJ INVALIDO!")

    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


x = Documento.valida_documento(48988752899)
print(x)
y = Documento.valida_documento(21220932000110)
print(y)