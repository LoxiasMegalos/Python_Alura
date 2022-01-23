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

print("*********************************************************")
#HERANÇAS!
class Veiculo:

    def __init__(self, nome):
        print("Deu certo")
        self._nome = nome

    def abastecer(self, litros):
        print("Abasteceu {} Litros".format(litros))


class Carro(Veiculo):
    def __init__(self, nome):
        self._nome = nome
    #def abastecer(self, litros):
        #pass

class Moto(Veiculo):
    def __init__(self, nome, motoboy = "joão"):
        super().__init__(nome)
        self._motoboy = motoboy

    @property
    def motoboy(self):
        return self._motoboy

Hornet = Moto("Hornet")
Hornet.abastecer(15)
print(Hornet.motoboy)

print()

Peugeot = Veiculo("Pejô")
Peugeot.abastecer(12)

print()

class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return print(f'Esse é um {cls.prefixo}')


Funcionario.info()

class FolhaDePagamento:
    @staticmethod
    def log():
        return print(f'Isso é um log qualquer')

FolhaDePagamento.log()

print()

lista = [1, 2, 4, 5]

print(repr(lista))

#METODOS MAGICOS:

class Listinha:

    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return self.items.__iter__()

    def __len__(self):
        return len(self.items)



meu_objeto = Listinha([1, 2, 4])

contador = 0
for item in meu_objeto:
    contador += 1

print(contador)
print(len(meu_objeto))

if len(meu_objeto) == contador:
    print('São iguais!')
else:
    print('Não são iguais!')

#classes ABC - Abstract Base Classes:

from collections.abc import Sized

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    #def __str__(self):
        #return self.descricao

    def __len__(self):
        return len(self.descricao)

x = [1,2,3,4,5]
lista = MinhaListagem(x)
print(lista)
print(len(lista))