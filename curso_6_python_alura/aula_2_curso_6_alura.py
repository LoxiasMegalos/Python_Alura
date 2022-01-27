lista = []

idades = [1,2,3,4,5]
idades.clear()   # Comando para remover tudo
idades.append(1) # Comando para adicionar apenas 1 termo no final da lista
idades2 = [2,3,4,5]
idades.extend(idades2) #Comando capaz de extender uma lista com outra lista

for idade in idades:  # Iteração Através de uma lista
    print(idade)

idades.remove(1) # Comando capaz de remover o termo procurado da lista, caso não tenha, vai dar erro, preferível utilizar com if

if(1 in idades): # Comparação em  listas - Verificando se um termo está dentro
    idades.remove(1)

print("Tamanho da lista", len(idades)) # Comando capaz de informar o tamanho de uma lista

idades_mais_1 = [(idade + 1) for idade in idades] # Compressão de listas - Criando uma nova lista com apenas 1 linha

print("Lista idades:", idades)
print("Lista idades +1", idades_mais_1)

def inicia_lista_parametro( lista = []):
    print(lista)
    print(len(lista))
    lista.append(1)

# As listas são objetos mutávei em python e seus valores internos serão alterados todas as vezes com base na função acima, o parâmetro inicial da função só irá ser válido na primeira vez que a função for chamada

def inicia_lista_none (lista = None): #Corrigimos o problema da lista mutar toda a vez que chamamos a função, pois agora a variável lista é nada, e atribuo o valor [] todas as vezes que a função é chamada
    if lista == None:
        lista = []
    print(lista)
    print(len(lista))
    lista.append(1)

#Objetos próprios

class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {} <<]".format(self.codigo, self.saldo)


conta_murillo = ContaCorrente(15)
print(conta_murillo)

conta_murillo.deposita(500)
print(conta_murillo)

conta_dani = ContaCorrente(47685)
conta_dani.deposita(1000)
print(conta_dani)

contas = [conta_murillo , conta_dani]

print(contas)

for conta in contas:
    print(conta)

contas = [conta_murillo,conta_dani, conta_murillo]
contas[2].deposita(300)

print(conta_murillo) #Listas são mutaveis e consigo alterar objetos diretamente com suas referencias, sendo necessário ter precaução.

contas = [conta_murillo , conta_dani]

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0,76)

conta_1 = (15, 1000) #tupla indicando o nº da conta e o saldo

def saldo_tupla(conta):
    valor = int(input("Quanto você quer depositar? "))
    novo_saldo = conta[1] + valor
    return (conta[0],novo_saldo)

#conta_1 = saldo_tupla(conta_1)

#print(conta_1)

#TUPLAS DE OBJETOS E LISTAS DE TUPLAS

murillo = ("Murillo",15,1000)
julia = ("Julia",12312, 100)

usuarios = [murillo, julia]
print(usuarios)

usuarios.append(("Edna", 4445, 999))

print(usuarios)

conta_murillo = ContaCorrente(15)
conta_murillo.deposita(100)
conta_julia = ContaCorrente(123)
conta_julia.deposita(99)

contas = (conta_murillo , conta_julia)

for conta in contas:
    print(conta)

contas[0].deposita(300) # Mesmo sendo uma tupla isso é possível pois a tupla nao deixa mudar a referencia dela, porém aqui eu alterei apenas 1 atributo dentro de 1 objeto, mas a tupla continua sendo imutável, nao costuma ser utilizada nesses cenários, pois com a lista seria a mesma coisa

