import a
import b

print("Faça a sua escolha: ")

def escolha():
    x = 0
    while(x == 0):
        decisao = input("Escolha a ou b: ")

        if(decisao == "a"):
            a.a()
        elif(decisao == "b"):
            b.b()
        else:
            print("Escolha uma opção válida")
            continue

        y = int(input("Quer Sair? (0) = Não | (1) = Sim: "))

        if(y == 1):
            x = 1
        elif(y == 0):
            continue
        else:
            print("Escolha uma opção válida")
            continue








if (__name__ == "__main__"):
    escolha()