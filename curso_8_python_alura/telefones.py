import re

#padrao = "[0-9][a-z][0-9]"
#url = "https://www.mokka-sensors.com.br/encoders"
#padrao_url = re.compile("(http(s)?://)?(www.)?mokka-sensors.com(.br)?/encoders")
#match = padrao_url.match(url)
#email = "\w{5,50}(.)?(\w{1,50})?@[a-z]{3,10}.\w{2,3}.(\w{2,3})?"
#texto = "aaaaaa@gmail.com.br"
#resposta = re.search(email, texto)
#print(resposta.group())

#padrao_molde = "(xx)aaaa-wwww"
#padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
#texto = "eu gosto do numero 1143183692 e gosto também do 11910009205"
#resposta = re.findall(padrao, texto)
#resposta = re.search(padrao, texto)
#print(resposta.group())

class TelefonesBr:

    def __init__(self, telefone):
        if(self.valida_telefone(telefone)):
            self.numero = telefone
        else:
            raise ValueError("Numero Incorreto!")

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if(resposta):
            return True
        else:
            return False

    def __str__(self):
        return self.format_numero()

    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado

#telefone = "11943220607"

#teste_class = TelefonesBr(telefone)
#print(teste_class)