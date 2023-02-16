#Projetinho

from datetime import date
data_atual  = date.today()
print(data_atual)

class Cor:

    def __str__(self):
        return "Cor: Branco, O {} tem uma velocidade máxima de {} km/h e já rodou {} quilometros".format(self.nome, self.velocidade, self.quilometragem)


class Veiculo(Cor):

    cor = "Branco"

    def __init__(self, nome, velocidade, quilometragem):
        self.nome = nome
        self.velocidade = velocidade
        self.quilometragem = quilometragem

    def capacidade(self, capacidade):
        return capacidade

    def fare(self):
        return self.capacidade() * 100

class Onibus(Veiculo):

    def __init__(self, nome, velocidade, quilometragem):
        super().__init__(nome, velocidade, quilometragem)

    def capacidade(self, capacidade = 50):
        return super().capacidade(capacidade=50)

    def fare(self):
        return (super().capacidade(capacidade=50) * 100) * 1.1



#Onibus1 = Onibus("Mercedes", 200, 100000)

#print(Onibus1)

#print(Onibus1.capacidade())

#print(Onibus1.fare())

#print(type(Onibus1))

#print(isinstance(Onibus1, Veiculo))

class TeAmo:
    def __str__(self):
        return "Te amo Em {}/{}/{} fomos na hamburgueria {} e pedimos um {}, Comentário: {}, Nota: {}".format(self.dia, self.mes, self.ano,self.lugar,self.pedido,self._comentario,self._nota)

class TeAmoP:
    def __str__(self):
        return "Te amo Em {}/{}/{} fomos no {} , Comentário: {}, Nota: {}".format(self.dia, self.mes, self.ano,self.lugar,self._comentario,self._nota)

class Passeios (TeAmoP):

    def __init__(self, lugar, dia, mes, ano):
        self.lugar = lugar
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self._comentario = "Nenhum comentario adicionado sobre {}".format(self.lugar)
        self._nota = 0

    def dar_comentario(self):
        self._comentario = input("O que você achou de {} ? ".format(self.lugar))

    def dar_nota(self):
        self._nota = input("Qual a nota do passeio {} ? ".format(self.lugar))

    @property
    def comentario(self):
        return self._comentario

    @property
    def nota(self):
        return self._nota

    def avaliacao(self):
        print("Em {}/{}/{} fomos em {}, Comentário: {}, Nota: {}".format(self.dia, self.mes, self.ano, self.lugar, self._comentario, self._nota ))

class Hamburgueria (Passeios,TeAmo):

    def __init__(self, lugar, dia, mes, ano, pedido):
        super().__init__(lugar, dia, mes, ano)
        self.pedido = pedido
        self._comentario = "Nenhum comentario adicionado sobre {}".format(self.lugar)
        self._nota = 0

    def dar_comentario(self):
        self._comentario = input("O que você achou da hamburgueria {} ? ". format(self.lugar))

    def dar_nota(self):
        self._nota = input("Qual a nota da hamburgueria {} ? ". format(self.lugar))

    @property
    def comentario(self):
        return self._comentario

    @property
    def nota(self):
        return self._nota

    #def __str__(self):
    #    print("Em {}/{}/{} fomos na hamburgueria {} e pedimos um {}, Comentário: {}, Nota: {}".format(self.dia, self.mes, self.ano, self.lugar, self.pedido, self._comentario, self._nota ))

    def avaliacao(self):
        print("Em {}/{}/{} fomos na hamburgueria {} e pedimos um {}, Comentário: {}, Nota: {}".format(self.dia, self.mes, self.ano, self.lugar, self.pedido, self._comentario, self._nota ))


