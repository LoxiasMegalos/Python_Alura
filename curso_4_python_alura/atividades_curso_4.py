class Pessoa:
    tamanho_cpf = 11




p = Pessoa()

print(p.tamanho_cpf)

p.tamanho_cpf = 12

print(p.tamanho_cpf) #É ALTERADO O VALOR DO TAMANHO CPF NA PESSOA p

print(Pessoa.tamanho_cpf) #O ATRIBUTO DA CLASSE NAO SE ALTERA
print("********************************************************************")

class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        print(self.nome)
        return True if len(self.cpf) == __class__.tamanho_cpf else False

pe = Pessoa('00000000001', 'Ruby')
print(pe.valida_cpf())
print()
pe = Pessoa('0000000000', 'Cristal')
print(pe.valida_cpf())