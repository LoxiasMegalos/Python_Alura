#AULA 2 CURSO 3 PYTHON ALURA - ORIENTAÇÃO A OBJETOS

def cria_conta( numero, titular, saldo, limite):
    conta = {"numero": numero , "titular" : titular, "saldo" : saldo, "limite" : limite}
    return conta
########################################################################
def deposita(conta, valor):
    conta["saldo"]+= valor
########################################################################
def saca(conta, valor):
    conta["saldo"] -= valor
#######################################################################
def extrato(conta):
    print("O seu extrato é {} R$".format(conta["saldo"]))

######################################################################
conta = cria_conta(123,"Murillo",1000.00, 1000.00)
#print(extrato(conta))
#deposita(conta, 90000)
#print(extrato(conta))
#print( conta["saldo"])
######################################################################

class ContaCorrente:

    def __init__(self, numero, titular, saldo, limite):
        #print("Construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = ContaCorrente(123, "Murillo", 55.0, 1000.0)
conta2 = ContaCorrente(321, "Murillo", 55.0, 1000.0)
print(conta)
print(conta2)
conta3 = ContaCorrente(1,"Eric Clapton", 0.0, 550.0)
print(conta3)
#ATRIBUTOS SÃO AS CARACTERÍSTICAS DE UMA CLASSE
print("Atributos são as características de uma classe")
##############################################
print()
print(conta.saldo)
print(conta3.saldo)