
from datetime import date, timedelta, time, tzinfo
'''
x = 13
y = 2
missa_1 = date(2022, y, x)
missa_domingo_1 = time(9,0)
missa_domingo_2 = time(10,30)
missa_domingo_3 = time(18,0)
#print(missa_1.strftime("%d/%m/%Y"))
#print(missa_domingo_1)
#print(missa_domingo_2)
#print(str(missa_domingo_3))

missas_domingo = [str(missa_domingo_1),str(missa_domingo_2),str(missa_domingo_3)]

semana = ["seg","ter","quar","quin","sex","sab","dom"]

verifica_dia = semana[missa_1.weekday()]
missas_fevereiro = []

if(verifica_dia == "dom"):
    for horario in missas_domingo:
        print(horario)
        missas_fevereiro.append((missa_1.strftime("%d/%m/%Y"), horario))

print(missas_fevereiro)
'''

class EscalaMes:

    def __init__(self, nome_mes):
        self.ano = 2022
        self.__mes = self.valida_mes(nome_mes)
        #self.dias = []
        #self.datas = []

    def valida_mes(self, nome_mes):

        meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]

        if(nome_mes in meses):
            return meses.index(nome_mes) + 1
        else:
            raise ValueError("Mês Inválido")


    @property
    def mes(self):
        return self.__mes
'''
    def define_dias(self, dias):
        for dia in dias:
            self.dias.append(dia)
        self.avalia_missas()

    def avalia_missas(self):
        for dia in self.dias:
            self.datas.append(date(self.ano, self.mes, dia))
'''

class DiasMissas:

    def __init__(self, mes ,dia):
        self.mes = mes
        self.dia = dia


#fevereiro = Escala_Mes("fev")
#fevereiro.define_dias([1,2,3,4,5,6,7])
#print(fevereiro.dias)
#print(fevereiro.datas)

mes_valido = 0
meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]
while(mes_valido == 0):
    mes = input("De qual mes vamos fazer a escala? ")
    if mes in meses:
        mes_valido = 1
        break
    print("Selecione um mês válido!")

cria_escala = EscalaMes(mes)
print(cria_escala.mes)
insere_dias = 0

while(insere_dias == 0):

