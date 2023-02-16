import re, requests, json, xlsxwriter, PySimpleGUI as sg

def limpa_cnpj(cnpj):
    cnpj_limpo = cnpj
    if "." in cnpj or "/" in cnpj or "-" in cnpj:
        cnpj_limpo = ""
        for digito in cnpj:
            try:
                teste = int(digito)
                cnpj_limpo = cnpj_limpo + str(teste)
            except ValueError:
                continue
    return cnpj_limpo

def identifica_cnpj(cnpj):
    padrao_cnpj = "[0-9]{2}(.)?[0-9]{3}(.)?[0-9]{3}(/)?[0-9]{4}(-)?[0-9]{2}"
    verifica_cnpj = re.search(padrao_cnpj, cnpj)

    while not verifica_cnpj:
        verifica_cnpj = re.search(padrao_cnpj, cnpj)
        if verifica_cnpj:
            break
        sg.change_look_and_feel('DarkAmber')

        layout = [[sg.Text('CORRIJA O CNPJ')],
                  [sg.Text('CNPJ', size=(4, 0)), sg.Input(size=(20, 0), key='cnpj')],
                  [sg.Button('Enviar Dados')]
                  ]

        janela = sg.Window("Padrão de CNPJ inválido", layout)

        button, values = janela.read()
        cnpj = values['cnpj']
        janela.close()

    return cnpj

def tipo_de_cadastro(verificacao_de_empreendimento):

    if (verificacao_de_empreendimento == 1):

        sg.change_look_and_feel('DarkAmber')

        layout = [[sg.Text('CADASTRO DE EMPRESA')],
                  [sg.Text('CNPJ',size=(20,0)),sg.Input(size=(20,0), key='cnpj')],
                  [sg.Text('Número da Empresa', size=(20, 0)), sg.Input(size=(4, 0), key='nemp')],
                  [sg.Button('Enviar Dados')]
                  ]

        janela = sg.Window("Cadastro de Empresa", layout)

        button, values = janela.read()
        cnpj = values['cnpj'].strip()
        emp = values['nemp']
        janela.close()

        #cnpj2 = input("Digite o CNPJ da empresa: ")
        #numero_secundario = input("Digite o número da Empresa: ")

        while len(emp) != 4:
            sg.change_look_and_feel('DarkAmber')

            layout = [[sg.Text('INSIRA O NUMERO DA EMPRESA COM 4 DIGITOS:')],
                      [sg.Text('Número da Empresa', size=(20, 0)), sg.Input(size=(4, 0), key='nemp')],
                      [sg.Button('Enviar Dados')]
                      ]

            janela = sg.Window("Correção Número do Empreendimento", layout)

            button, values = janela.read()
            emp = values['nemp']
            janela.close()

        cnpj_consulta = identifica_cnpj(cnpj)
        cnpj_consulta = limpa_cnpj(cnpj_consulta)

        #print(cnpj_consulta)
        cria_relatorio_empresa(cnpj_consulta, emp, verificacao_de_empreendimento)

    elif (verificacao_de_empreendimento == 2):

        sg.change_look_and_feel('DarkAmber')

        layout = [[sg.Text('CADASTRO DE DIVISÃO')],
                  [sg.Text('CNPJ', size=(30, 0)), sg.Input(size=(20, 0), key='cnpj')],
                  [sg.Text('Número da Empresa - Ligada a Divisão', size=(30, 0)), sg.Input(size=(4, 0), key='nemp')],
                  [sg.Text('Número da Divisão', size=(30, 0)), sg.Input(size=(4, 0), key='div')],
                  [sg.Button('Enviar Dados')]
                  ]

        janela = sg.Window("Cadastro de Empresa", layout)

        button, values = janela.read()
        cnpj = values['cnpj'].strip()
        emp = values['nemp']
        div = values['div']

        janela.close()
        #cnpj2 = input("Digite o CNPJ da Divisão: ")
        #numero_secundario = input("Digite o número da Empresa - Ligada a Divisão: ")
        #numero_div = input("Digite o número da Divisao: ")

        while len(emp) != 4:
            sg.change_look_and_feel('DarkAmber')

            layout = [[sg.Text('INSIRA O NUMERO DA EMPRESA COM 4 DIGITOS:')],
                      [sg.Text('Número da Empresa', size=(20, 0)), sg.Input(size=(4, 0), key='nemp')],
                      [sg.Button('Enviar Dados')]
                      ]

            janela = sg.Window("Correção Número do Empreendimento", layout)

            button, values = janela.read()
            emp = values['nemp']
            janela.close()

        while len(div) != 4:
            sg.change_look_and_feel('DarkAmber')

            layout = [[sg.Text('INSIRA O NUMERO DA DIVISÃO COM 4 DIGITOS:')],
                      [sg.Text('Número da Divisão', size=(20, 0)), sg.Input(size=(4, 0), key='div')],
                      [sg.Button('Enviar Dados')]
                      ]

            janela = sg.Window("Correção Número da Divisão", layout)

            button, values = janela.read()
            div = values['div']
            janela.close()

        cnpj_consulta = identifica_cnpj(cnpj)
        cnpj_consulta = limpa_cnpj(cnpj_consulta)

        #print(cnpj_consulta)
        cria_relatorio_divisao(cnpj_consulta, emp, div, verificacao_de_empreendimento)

    elif (verificacao_de_empreendimento == 3):

        sg.change_look_and_feel('DarkAmber')

        layout = [[sg.Text('CADASTRO DE FILIAL')],
                  [sg.Text('CNPJ', size=(30, 0)), sg.Input(size=(20, 0), key='cnpj')],
                  [sg.Text('Número da Empresa - Ligada a Filial', size=(30, 0)), sg.Input(size=(4, 0), key='nemp')],
                  [sg.Text('Número da Filial', size=(30, 0)), sg.Input(size=(4, 0), key='fil')],
                  [sg.Button('Enviar Dados')]
                  ]

        janela = sg.Window("Cadastro de Empresa", layout)

        button, values = janela.read()
        cnpj = values['cnpj'].strip()
        emp = values['nemp']
        fil = values['fil']

        janela.close()
        #cnpj2 = input("Digite o CNPJ da Filial: ")
        #numero_secundario = input("Digite o número da Empresa - Ligada a Filial: ")
        #numero_fil = input("Digite o número da Filial: ")

        while len(emp) != 4:
            sg.change_look_and_feel('DarkAmber')

            layout = [[sg.Text('INSIRA O NUMERO DA EMPRESA COM 4 DIGITOS:')],
                      [sg.Text('Número da Empresa', size=(20, 0)), sg.Input(size=(4, 0), key='nemp')],
                      [sg.Button('Enviar Dados')]
                      ]

            janela = sg.Window("Correção Número do Empreendimento", layout)

            button, values = janela.read()
            emp = values['nemp']
            janela.close()

        while len(fil) != 4:
            sg.change_look_and_feel('DarkAmber')

            layout = [[sg.Text('INSIRA O NUMERO DA FILIAL COM 4 DIGITOS:')],
                      [sg.Text('Número da Filial', size=(20, 0)), sg.Input(size=(4, 0), key='fil')],
                      [sg.Button('Enviar Dados')]
                      ]

            janela = sg.Window("Correção Número da Filial", layout)

            button, values = janela.read()
            fil = values['fil']
            janela.close()

        cnpj_consulta = identifica_cnpj(cnpj)
        cnpj_consulta = limpa_cnpj(cnpj_consulta)

        #print(cnpj_consulta)
        cria_relatorio_filial(cnpj_consulta, emp, fil, verificacao_de_empreendimento)

def corrige_nome_empreendimento(nome):
    tratando_nome = ""
    nome_atualizado_30 = ""
    nome_atualizado_20 = ""
    nome_atualizado_25 = ""

    for letra in nome.replace(".", "").replace("EMPREENDIMENTOS", "EMP").replace("IMOBILIARIOS", "IMOB").replace("COMERCIO", "COM").replace("CONSUMO", "CONS"):
        tratando_nome = tratando_nome + letra
        if letra == " ":
            if (len(nome_atualizado_30) + len(tratando_nome) <= 30) and len(tratando_nome.strip()) > 1:
                nome_atualizado_30 = nome_atualizado_30 + tratando_nome
            if (len(nome_atualizado_25) + len(tratando_nome) <= 25 and len(tratando_nome.strip()) > 1):
                nome_atualizado_25 = nome_atualizado_25 + tratando_nome
            if (len(nome_atualizado_20) + len(tratando_nome) <= 20 and len(tratando_nome.strip()) > 1):
                nome_atualizado_20 = nome_atualizado_20 + tratando_nome
            tratando_nome = ""

    if (len(nome_atualizado_30) + len(tratando_nome) <= 30):
        nome_atualizado_30 = nome_atualizado_30 + tratando_nome
    if (len(nome_atualizado_25) + len(tratando_nome) <= 25):
        nome_atualizado_25 = nome_atualizado_25 + tratando_nome
    if (len(nome_atualizado_20) + len(tratando_nome) <= 20):
        nome_atualizado_20 = nome_atualizado_20 + tratando_nome

    return nome_atualizado_30, nome_atualizado_25, nome_atualizado_20

def cria_relatorio_empresa(cnpj_consulta, numero, tipo):

    consulta = "https://www.receitaws.com.br/v1/cnpj/{}".format(cnpj_consulta)
    consulta_api = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"}
    response = requests.request("GET", consulta, params=consulta_api)
    resp = json.loads(response.text)
    resp = resp

    nome_atualizado_30, nome_atualizado_25, nome_atualizado_20 = corrige_nome_empreendimento(resp['nome'])

    cadastro = [numero, numero, numero, numero, numero, resp['cep'].replace(".",""), nome_atualizado_30, nome_atualizado_20,
                "Área administ.financ."+numero, nome_atualizado_25, nome_atualizado_20, numero, numero, numero, numero,
                numero, numero, "ISENTO", "C"+numero+"0", resp['municipio'], numero, cnpj_consulta, "FK"+numero, nome_atualizado_30,
                nome_atualizado_30,nome_atualizado_30,nome_atualizado_30,numero, resp['uf'], resp['logradouro']+", "+resp['numero'],
                numero, numero, cnpj_consulta[:8], numero]

    relatorio(tipo, numero, cadastro)

def cria_relatorio_divisao(cnpj_consulta, numero, numero_div, tipo):

    consulta = "https://www.receitaws.com.br/v1/cnpj/{}".format(cnpj_consulta)
    consulta_api = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"}
    response = requests.request("GET", consulta, params=consulta_api)
    resp = json.loads(response.text)
    resp = resp

    #sg.change_look_and_feel('DarkAmber')

    #layout = [[sg.Text('LOCAL DE NEGOCIOS')],
    #          [sg.Text('Digite o Local de Negocios - Divisão:', size=(40, 0)), sg.Input(size=(4, 0), key='ln')],
    #          [sg.Button('Enviar Dados')]
    #          ]

    #janela = sg.Window("Local de Negocios", layout)

    #button, values = janela.read()
    #local_negocio_cnpj = values['ln']
    #janela.close()

    local_negocio_cnpj = cnpj_consulta[8:12]

    nome_atualizado_30, nome_atualizado_25, nome_atualizado_20 = corrige_nome_empreendimento(resp['nome'])

    cadastro = [numero_div, numero_div, cnpj_consulta, resp['cep'].replace(".",""), nome_atualizado_20,
                nome_atualizado_30, numero_div, numero, "ISENTO", resp['municipio'], numero_div, local_negocio_cnpj,
                nome_atualizado_30, nome_atualizado_30,nome_atualizado_30,numero_div, resp['uf'], resp['logradouro']+", "+resp['numero']]

    relatorio(tipo, numero_div, cadastro)


def cria_relatorio_filial(cnpj_consulta, numero, numero_fil, tipo):

    consulta = "https://www.receitaws.com.br/v1/cnpj/{}".format(cnpj_consulta)
    consulta_api = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"}
    response = requests.request("GET", consulta, params=consulta_api)
    resp = json.loads(response.text)
    resp = resp

    #sg.change_look_and_feel('DarkAmber')

    #layout = [[sg.Text('LOCAL DE NEGOCIOS')],
    #          [sg.Text('Digite o Local de Negocios - Filial:', size=(40, 0)), sg.Input(size=(4, 0), key='ln')],
    #          [sg.Button('Enviar Dados')]
    #          ]

    #janela = sg.Window("Local de Negocios", layout)

    #button, values = janela.read()
    #local_negocio_cnpj = values['ln']
    #janela.close()

    local_negocio_cnpj = numero_fil

    nome_atualizado_30, nome_atualizado_25, nome_atualizado_20 = corrige_nome_empreendimento(resp['nome'])

    cadastro = [numero_fil, numero_fil, cnpj_consulta, resp['cep'].replace(".", ""), "", nome_atualizado_20,
                nome_atualizado_30, numero_fil, numero, "ISENTO", resp['municipio'], numero_fil, local_negocio_cnpj,
                nome_atualizado_30, nome_atualizado_30, nome_atualizado_30, numero_fil, resp['uf'],
                resp['logradouro'] + ", " + resp['numero']]

    sg.change_look_and_feel('DarkAmber')

    layout = [[sg.Text('CADASTRO DE FILIAL - NOTA FISCAL')],
              [sg.Text('Emite Nota Fiscal?')],
              [sg.Radio('SIM', 'escolha', key='s'), sg.Radio('NÃO', 'escolha', key='n')],
              [sg.Button('Enviar Dados')]
              ]

    janela = sg.Window("Verifica NF", layout)

    button, values = janela.read()
    s = values['s']
    n = values['n']

    janela.close()

    if s:
        #org = int(input("Digite qual será a organização de vendas - Apenas números: "))


        #sg.change_look_and_feel('DarkAmber')

        # = [[sg.Text('Organização de Vendas')],
        #          [sg.Text('Digite a Organização de Vendas - Filial:', size=(40, 0)), sg.Input(size=(2, 0), key='org')],
        #          [sg.Button('Enviar Dados')]
        #          ]

        #janela = sg.Window("Organização de Vendas", layout)

        #button, values = janela.read()
        #org = values['org']
        #janela.close()

        org = numero_fil
        cadastro_nf = [numero_fil, nome_atualizado_20, org+"/"+numero+"/"+numero_fil+"-Saída", numero,
                      org+"SA", numero_fil,org, org, org+"SA"]
        relatorio_filial_nota_fiscal(numero_fil, cadastro_nf)
        #cadastro.append(numero_fil)
        relatorio(tipo, numero_fil, cadastro)
    else:
    #    cadastro.append("Não Emite NF")
        relatorio(tipo, numero_fil, cadastro)


def relatorio(tipo, numero, lista_cadastro):

    if tipo == 1:
        rotulos = ["Área Contábil", "Área de AF", "Área de Avaliação", "Característica de Agrupamento", "Centro", "Código Postal", "Denominação 30 caracteres",
                   "Denominação 20 caracteres", "Den. área.admin.finan", "Den. de área de contabilidade", "Den. da firma ou empresa", "Empresa", "Empresa",
                   "Empresa de ref para advertências", "Empresa do modelo", "Empresa Pagadora", "Empresa para atrib de nºs", "Inscrição Municipal", "Joint Venture",
                   "Local", "Local de Negócios", "Nº ID Fiscal 1", "NºObjeto", "Nome 30 caracteres", "Nome 30 caracteres", "Nome 30 caracteres", "Nome da Soci 30 caracteres",
                   "Organização de compras", "Região", "Rua e nº", "Sociedade", "Valor de Parametros", "CNPJ 8 Digitos","Var.períodos contábil"]
    elif tipo == 2:
        rotulos = ["Área de Avaliação", "Centro", "CNPJ", "Código Postal", "Denominação", "Denominação da divisão", "Divisão", "Empresa",
                   "Incrição Municipal", "Local", "Local de Negócios", "Local de Negócios CNPJ", "Nome", "Nome 1", "Nome 2",
                   "Organiz.compas", "Região", "Rua e nº"]
    else:
        rotulos = ["Área de Avaliação", "Centro", "CNPJ", "Código Postal", "CxPostal", "Denominação 20 caracteres", "Denominação 30 caracteres", "Filial", "Empresa",
                   "Incrição Municipal", "Local", "Local de Negócios", "Local de Negócios CNPJ", "Nome 30 caracteres", "Nome 30 caracteres", "Nome 30 caracteres",
                   "Organiz.compas", "Região(estado)", "Rua e nº"]

    #workbook = xlsxwriter.Workbook("../Projetos_Murillo/Empresa.xlsx")
    workbook = xlsxwriter.Workbook("Empresa2.xlsx")
    worksheet = workbook.add_worksheet("BC SET {}".format(numero))
    worksheet.protect()

    liberado = workbook.add_format({'locked': False, 'border': 1, 'border_color': 'black'})
    centro = workbook.add_format({"align": "center","pattern": 1,"bg_color":'#CCCCCC', "border": 1,"border_color": "black"})
    avaliacao = workbook.add_format({"align": "center", "border": 1, "border_color": "black"})


    # Criando Títulos de Colunas
    # worksheet.write("A1", "Cadastro")
    # Criando dados no arquivo

    worksheet.write(0, 0, "Rótulos", centro)
    worksheet.write(0, 1, "Variáveis", centro)
    worksheet.write(0, 2, "Informar se o dado precisa de revisão", avaliacao)

    for info in range(len(lista_cadastro)):
        worksheet.write(info + 1, 0, rotulos[info], centro)
        worksheet.write(info + 1, 1, lista_cadastro[info], centro)
        worksheet.write(info + 1, 2, "", liberado)
    worksheet.set_column("A:A", 35)
    worksheet.set_column("B:B", 30)
    worksheet.set_column("C:C", 40)
    workbook.close()

def relatorio_filial_nota_fiscal(numero, lista_cadastro):

    workbook = xlsxwriter.Workbook("BC_SET_Filial_NF.xlsx")
    worksheet = workbook.add_worksheet("BC SET {} NF".format(numero))
    worksheet.protect()

    protegidos = workbook.add_format({"align": "center","pattern": 1,"bg_color":'#CCCCCC', "border": 1,"border_color": "black"})
    avalicao_topo = workbook.add_format({"align": "center", "border": 1, "border_color": "black"})
    avalicao = workbook.add_format({'locked': False, 'border': 1, 'border_color': 'black'})

    rotulos = ["Centro", "Denominação", "Descr/Empresa/Filial", "Empresa", "Organização de Vendas SA", "Filial", "Organização de Vendas",
               "Tipo de Org de Vendas", "Valor do subobjeto"]

    # Criando Títulos de Colunas
    # worksheet.write("A1", "Cadastro")
    # Criando dados no arquivo

    worksheet.write(0, 0,  "Rótulos:", protegidos)
    worksheet.write(0, 1, "Variáveis:", protegidos)
    worksheet.write(0, 2, "Avaliação:", avalicao_topo)

    for info in range(len(lista_cadastro)):
        worksheet.write(1+info, 0, rotulos[info], protegidos)
        worksheet.write(1+info, 1, lista_cadastro[info], protegidos)
        worksheet.write(1+info, 2, "", avalicao)

    worksheet.set_column("A:A", 35)
    worksheet.set_column("B:B", 35)
    worksheet.set_column("C:C", 35)
    workbook.close()

#verificacao_de_empreendimento = int(input("Digite o tipo de empreendimento: (1) Empresa | (2) Divisão | (3) Filial | Demais Opções resultam em erro! "))
#tipo_de_cadastro(verificacao_de_empreendimento)

def proximaTela(emp, div, fil):
    if emp and not fil and not div:
        #print("Selecionou cadastro de Empresa")
        tipo_de_cadastro(1)
    elif not emp and fil and not div:
        #print("Selecionou cadastro de Filial")
        tipo_de_cadastro(3)
    elif not emp and not fil and div:
        #print("Selecionou cadastro de Divião")
        tipo_de_cadastro(2)


def tela_de_selecao():
    sg.change_look_and_feel('DarkAmber')

    layout = [[sg.Text('Qual será o tipo de cadastro? - Selecione apenas uma opção!')],
            [sg.Radio('Empresa','escolha',key='empresa'), sg.Radio('Divisão','escolha', key='div'),sg.Radio('Filial', 'escolha',key='fil')],
            [sg.Button('Enviar Dados')]
    ]

    janela = sg.Window("Seleção de Cadastro", layout)

    button, values = janela.read()
    emp = values['empresa']
    div = values['div']
    fil = values['fil']
    janela.close()
    proximaTela(emp, div, fil)
    janela.close()

tela_de_selecao()

