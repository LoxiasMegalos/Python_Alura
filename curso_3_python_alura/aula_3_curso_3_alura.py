print()

class Jogo:

    def __init__(self):
        self.contador = 0

    def incrementa(self):
        self.contador += 1
        print("incrementando")

class Pessoa:

    def __init__(self, nome, sobrenome):
        print("Nomeando {} em {}".format(nome, self))
        self.nome = nome
        self.sobrenome = sobrenome

    def imprime_nome(self):
        print("{} {}".format(self.nome, self.sobrenome))

    def nome_americano(self):
        print("{1} {0}".format(self.nome, self.sobrenome))

class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.00):
        print("Criando conta de {1}... em {0}".format(self,titular))
        print()
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))
        print()

    def deposita(self, valor):
        self.saldo += valor
        print("Foi de Depositado {}R$ em sua conta {} ".format(valor, self.titular))
        print()

    def saca(self, valor):
        verifica = self.saldo - valor
        if(verifica < -self.limite):
            print("{} Sua conta tem um limite de {} R$, Transação Bloqueada".format(self.titular, self.limite))
        else:
            self.saldo -= valor
            print("Foi Sacado {1}R$ da sua conta {0} ".format(self.titular, valor))

class Recibo:

    def __init__(self, valor, numero):
        print("Colocando {} R$ do recibo {}". format(valor, numero))
        self.valor = valor
        self.numero = numero

    def imprime_recibo(self):
        print("O valor do recibo {} é: {}".format(self.numero, self.valor))
        print()

class Sistema:

    def __init__(self):
        self.texto = ''

    def le_entrada(self):
        self.texto = input("Digite: ")

    def exibe_saida(self):
        print(self.texto)

class Data:

    def __init__(self, dia, mes, ano):
        print("Adicionando Data em {}".format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatadata(self):
        print("{}/{}/{}".format(self.dia,self.mes,self.ano))
        print("ou")
        print(self.dia,self.mes,self.ano, sep="/")
        print()

conta = Conta(1,"Murillo",500.00)
#print(conta.saldo)
#print(conta.limite)
#print()
conta2 = Conta(2,"Julia", 1000.00, 3000.00)
#print(conta2.saldo)
#print(conta2.limite)
#rint()
conta.extrato()
conta2.extrato()
conta.deposita(300)
conta.extrato()
conta.saca(10000)
conta.extrato()



jogo = Jogo()
jogo.incrementa()
print(jogo.contador)
jogo2 = Jogo()
jogo2.incrementa()
jogo2.incrementa()
jogo2.incrementa()
jogo2.incrementa()
print(jogo.contador)
print(jogo2.contador)


nome = Pessoa("Murillo", "Alcantara")
nome.nome_americano()
nome.imprime_nome()
print(nome.nome, " - Acessando o atributo nome dentro da variável de referencia, sem utilizar métodos")

print()
outra_ref = conta
print(outra_ref)
print("O tipo é: ", type(outra_ref))
outra_ref = None
print(outra_ref)
print("O tipo agora é: ", type(outra_ref))
print()

recibo1 = Recibo(50,1)
recibo2 = Recibo(100,2)
recibo3 = Recibo(200,3)
recibo4 = recibo3
recibo3 = None
recibo1 = recibo3
recibo4 = recibo1
recibo3 = recibo2

#recibo1.imprime_recibo()
recibo2.imprime_recibo()
recibo3.imprime_recibo()
#recibo4.imprime_recibo()

texto = Sistema()
texto.le_entrada()
texto.exibe_saida()

print("Comecei a Namorar em: ")
inicio = Data(15,11,2021)
inicio.formatadata()
print("Vou completar um ano em: ")
um_ano = Data(15,11,2022)
um_ano.formatadata()