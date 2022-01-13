#PRIMEIRA AULA DO CURSO 3 DA FORMAÇÃO DE PYTHON ALURA
#Orientação a objetos
#CONTA BANCÁRIA

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))


#COMO FAZER ISSO PARA MAIS CONTAS?

#precisamos de ujma função

conta = cria_conta(123, "Murillo", 55.0, 1000.00)
conta["saldo"]
deposita(conta, 15.0)
extrato(conta)
saca(conta, 20.0)
extrato(conta)
