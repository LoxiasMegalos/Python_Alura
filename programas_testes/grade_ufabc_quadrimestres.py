from datetime import datetime

hoje = datetime.today()
print(hoje)
semana = ["segunda","terca","quarta","quinta","sexta","sabado","domingo"]
print(semana[hoje.weekday()])

class GradeUfabc:

    def __init__(self, dia, aulas):
        #print("Criando objeto em {}".format(self))
        self.dia = self.verifica_dia(dia)
        self.aulas = aulas

    def verifica_dia(self, dia):
        semana = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]
        if(dia in semana):
            return dia
        else:
            raise ValueError("Dia inválido!")

    def __str__(self):
        return "hoje é {} e suas aulas são: {}".format(self.dia, self.aulas)

'''
aulas_dia = []
dias_aulas = list()
for dia in semana:
    if(dia != "sabado" and dia != "domingo"):
        quantidade_de_aulas = int(input("Quantas aulas tem na {} ? ".format(dia)))
    else:
        continue
    for quantidade in range(0,quantidade_de_aulas):
        aula = input("Digite a {}º matéria de {} ".format(quantidade+1, dia))
        aulas_dia.append(aula)

    dias_aulas.append(GradeUfabc(dia, aulas_dia))
    aulas_dia = []
'''
#print(dias_aulas)

dias_aulas = []
segunda = GradeUfabc("segunda",["Matemática Discreta", "Sistemas Operacionais"])
terca = GradeUfabc("terca",["Algoritmos"])
quarta = GradeUfabc("quarta",["Circuitos Digitais"])
quinta = GradeUfabc("quinta",["Matemática Discreta", "Sistemas Operacionais"])
sexta = GradeUfabc("sexta",["Circuitos Digitais", "Algoritmos"])
sabado = GradeUfabc("sabado",["HOJE NÃO TEM FACULDADE"])
domingo = GradeUfabc("domingo",["HOJE NÃO TEM FACULDADE"])

dias_aulas.append(segunda)
dias_aulas.append(terca)
dias_aulas.append(quarta)
dias_aulas.append(quinta)
dias_aulas.append(sexta)
dias_aulas.append(sabado)
dias_aulas.append(domingo)

for dia in range (0,len(dias_aulas)):
    if(dia == hoje.weekday()):
        print(dias_aulas[dia])