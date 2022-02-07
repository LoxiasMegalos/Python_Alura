from datetime import datetime, timedelta

#print(datetime.today())

class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadasto_str(self):
        meses_do_ano = ["jan","fev","mar","abr","mai","jun","jul","ago","set","oct","nov","dez"]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def mes_cadasto(self):
        mes_cadastro = self.momento_cadastro.month
        return mes_cadastro

    @property
    def dia_semana(self):
        dia_semana_lista = ["seg","ter","quar","quinta","sex","sab","domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days = 30)) - self.momento_cadastro
        return tempo_cadastro

'''
hoje= datetime.today()
print(hoje)
hoje_formatado = hoje.strftime("%d/%m/%Y  %H:%M")
print(hoje_formatado)
print(type(hoje_formatado))

print(1)
'''
