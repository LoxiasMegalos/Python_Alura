nome = input("Informe seu nome: ")
salario = float(input("Salario: "))
vendas = float(input("Resultado das vendas: "))

bonus = salario + (0.15 * vendas)

print("TOTAL = R$ {:.2f}".format(bonus))