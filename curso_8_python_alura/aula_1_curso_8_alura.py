#Python Brasil
#Criação de uma biblioteca de classes para validade diversas informações, utilizando orientação a objetos, padrões pela biblioteca re, timedata, e APIS

#VALIDAÇÃO DE UM CPF
import re

from CPF_CNPJ import Documento
#from treinando_curso_8 import CpfTeste
cnpj_um = Documento.cria_documento(21220932000110)
#cpf_dois = Cpf(111111111121)
print(cnpj_um)

documento = Documento.cria_documento(48988752899)
print(documento)

from telefones import TelefonesBr

telefone = "551143183692"

telefone_objeto = TelefonesBr(telefone)
#print(telefone_objeto.numero)
print(telefone_objeto)
#print(telefone_objeto)
#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao, telefone)
#print(resposta.group(1,2,3,4))