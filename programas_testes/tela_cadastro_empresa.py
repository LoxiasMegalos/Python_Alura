import PySimpleGUI as sg

class TelaPython:

    def __init__(self):
        sg.change_look_and_feel('DarkAmber')
        #Layout
        layout = [
            [sg.Text('Nome',size=(10,0)),sg.Input(size=(15,0), key='nome')],
            [sg.Text('Numero',size=(10,0)),sg.Input(size=(4,0), key='idade')],
            [sg.Text('Quais Provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('OutLook',key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita Cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaC'),sg.Radio('Não', 'cartoes', key='naceitaC')],
            [sg.Slider(range=(0,255), default_value=0, orientation='h',size=(15,20), key='slider_velocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        #Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        #Extrair dados da tela


    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_ol = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao_sim = self.values['aceitaC']
            aceita_cartao_nao = self.values['naceitaC']
            velocidade_script = self.values['slider_velocidade']
            print("nome: {}".format(nome))
            print("idade: {}".format(idade))
            print("aceita_outlook: {}".format(aceita_ol))
            print("aceita_gmail: {}".format(aceita_gmail))
            print("aceita_yahoo: {}".format(aceita_yahoo))
            print("Aceita Cartao Sim: {}".format(aceita_cartao_sim))
            print("Aceita Cartao Nao: {}".format(aceita_cartao_nao))
            print("Velocidade Script: {}".format(velocidade_script))


#tela = TelaPython()
#tela.Iniciar()


class SelecaoCadastro:

    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Qual será o tipo de cadastro? - Selecione apenas uma opção!')],
            [sg.Checkbox('Empresa', key='empresa'), sg.Checkbox('Divisão', key='div'),
             sg.Checkbox('Filial', key='fil')],
            [sg.Button('Enviar Dados')]
        ]
        # Janela
        janela = sg.Window("Seleção de Cadastro").layout(layout)
        # Extrair dados da tela
        self.button, self.values = janela.Read()

    def iniciar(self):

        emp = self.values['empresa']
        div = self.values['div']
        fil = self.values['fil']

        print("Cadastro Empresa: {}".format(emp))
        print("Cadastro Divisão: {}".format(div))
        print("Cadastro Filial: {}".format(fil))

        self.proximaTela(emp, div, fil)

    def proximaTela(self, emp, div, fil):
        if emp and not fil and not div:
            print("Selecionou cadastro de Empresa")
        elif not emp and fil and not div:
            print("Selecionou cadastro de Filial")
        elif not emp and not fil and div:
            print("Selecionou cadastro de Divião")
        else:
            print("Selecione apenas 1 Opção!")
            raise ValueError("Mais de Uma Opção Selecionada")


#seleciona = SelecaoCadastro()
#seleciona.iniciar()

#seleciona.values['empresa']


# Layout


def proximaTela(emp, div, fil):
    if emp and not fil and not div:
        print("Selecionou cadastro de Empresa")
    elif not emp and fil and not div:
        print("Selecionou cadastro de Filial")
    elif not emp and not fil and div:
        print("Selecionou cadastro de Divião")
    else:
        print("Selecione apenas 1 Opção!")
        raise ValueError("Mais de Uma Opção Selecionada")

sg.change_look_and_feel('DarkAmber')

layout = [[sg.Text('Qual será o tipo de cadastro? - Selecione apenas uma opção!')],
        [sg.Radio('Empresa','escolha',key='empresa'), sg.Radio('Divisão','escolha', key='div'),sg.Radio('Filial', 'escolha',key='fil')],
        [sg.Button('Enviar Dados')]
]

janela = sg.Window("Seleção de Cadastro", layout)

while True:
    button, values = janela.read()
    emp = values['empresa']
    div = values['div']
    fil = values['fil']
    proximaTela(emp, div, fil)

janela.close()