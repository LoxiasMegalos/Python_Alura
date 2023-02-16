import re

texto = '''
'''

telefone = '94322-0607'
padrao = "[0-9]{5}-[0-9]{4}"
verifica = re.search(padrao, telefone)
print(verifica.group())

conta = 'safra 12341-62'
banco = '[a-z]{1,200}'
verifica_banco = re.search(banco, conta);
print(verifica_banco.group())
if(verifica_banco.group() == "itau"):
    padrao_conta = '[0-9]{7}'
    padrao_agencia = '(-[0-9]{3})'
    verifica_conta = re.search(padrao_conta, conta)
    verifica_agencia = re.search(padrao_agencia, conta)
else:
    padrao_conta = '[0-9]{5}'
    padrao_agencia = '-[0-9]{2}'
    verifica_conta = re.search(padrao_conta, conta)
    verifica_agencia = re.search(padrao_agencia, conta)

print("O banco é o {}, a conta é a número {} e a agencia numero {}".format(verifica_banco.group(),verifica_conta.group(),verifica_agencia.group()[1:]))
