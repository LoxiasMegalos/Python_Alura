from aula_1_curso_9_alura import Usuario, Lance, Leilao, Avaliador

murillo = Usuario("Murillo")
yuri = Usuario("Yuri")

lance_do_murillo = Lance(murillo, 1000.0)
lance_do_yuri = Lance(yuri, 100.0)

leilao = Leilao("Celular")
leilao.lances.append(lance_do_murillo)
leilao.lances.append(lance_do_yuri)



#for lance in leilao.lances:
#    print("O usuario {} deu um lance de {} R$".format(lance.usuario.nome, lance.valor))

#avaliador = Avaliador()
#avaliador.avalia(leilao)
#print(avaliador.menor_lance)
#print(avaliador.maior_lance)