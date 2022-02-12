def time_calculator(tempo_inicio, tempo_adicional, dia_inicio = ""):
    #tempo_inicio = "11:43 AM"
    #tempo_adicional = "00:20"
    periodo_inicial = "AM" if "AM" in tempo_inicio else "PM"

    hora_inicio = 0
    minuto_inicio = 0
    hora_adicional = 0
    #minuto_adicional = 0
    dias_pulados = 0

    #SEPARA A HORA DOS MINUTOS DO TEMPO INICIAL
    verifica = ""
    for tempo in tempo_inicio:
        verifica += tempo
        if(tempo == ":"):
            hora_inicio = int(verifica[:-1].strip())
            verifica = ""
        elif(tempo == "A" or tempo == "P"):
            minuto_inicio = int(verifica[:-1].strip())

    #SEPARA A HORA DOS MINUTOS DO TEMPO ADICIONAL
    verifica = ""
    for tempo in tempo_adicional:
        verifica += tempo
        if(tempo == ":"):
            hora_adicional = int(verifica[:-1].strip())
            verifica = ""
    minuto_adicional = int(verifica.strip())

    #VERIFICA OS MINUTOS E SE TEM HORAS ADICIONAIS GRAÇAS A SOMATORIA DE MINUTOS
    minutos = minuto_inicio + minuto_adicional
    if(minutos >= 60):
        minutos_finais = minutos % 60
        horas_minutos = 1
    else:
        minutos_finais = minutos
        horas_minutos = 0

    #VERIFICA AS HORAS FINAIS E QUANTOS PERIODOS DE 12 HORAS PASSARAM
    horas_totais = horas_minutos + hora_inicio + hora_adicional
    #print(horas_totais, "horas totais")
    if horas_totais < 12:
        hora_final = horas_totais
        trocas = 0
    else:
        hora_final = int(horas_totais/(horas_totais/12)) if horas_totais % 12 == 0 else horas_totais % 12
        #print("a hora final é:", hora_final)
        trocas = int(horas_totais/12) if hora_inicio % 12 != 0 or hora_adicional % 12 != 0 else int(horas_totais/12) -1
        #print("são", trocas, "trocas")


    #VERIFICA QUANTOS DIAS PASSARAM COM A ADIÇÃO DE TEMPO
    if trocas % 2 != 0:
        if periodo_inicial == "AM":
            periodo_final = "PM"
            if(trocas > 1):
                dias_pulados = trocas//2
        elif periodo_inicial == "PM":
            dias_pulados = 1 + trocas//2
            #print("dias pulados", dias_pulados)
            periodo_final = "AM"
    else:
        periodo_final = periodo_inicial
        dias_pulados = trocas//2

    #print(hora_final,":", minutos_finais, " ", periodo_final)

    semana = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dia_inicio = dia_inicio.lower().title()


    if(dia_inicio in semana):
        index = 0
        for dia in semana:
            if dia == dia_inicio:
                if(index + dias_pulados >= 7):
                    semana_final = semana[(index + dias_pulados) % 7]
                else:
                    semana_final = semana[index + dias_pulados]
            index += 1

    if(dias_pulados == 1):
        dia_final = "Próximo Dia"
    elif(dias_pulados == 0):
        dia_final = ""
    else:
        pulos = str(dias_pulados)
        dia_final = pulos + " dias depois"

    if(dia_inicio == "" and dias_pulados == 0):
        print("{}:{:02d} {}".format(hora_final, minutos_finais, periodo_final))
    elif(dia_inicio == "" and dias_pulados != 0):
        print("{}:{:02d} {} ({})".format(hora_final,minutos_finais,periodo_final,dia_final))
    elif(dia_inicio != "" and dias_pulados == 0):
        print("{}:{:02d} {}, {}".format(hora_final,minutos_finais,periodo_final,semana_final))
    else:
        print("{}:{:02d} {}, {} ({})".format(hora_final,minutos_finais,periodo_final,semana_final,dia_final))

if __name__ == "__main__":
    time_calculator()