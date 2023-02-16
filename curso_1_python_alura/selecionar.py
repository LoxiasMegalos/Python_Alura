import b
import c


print("*******************************************", end="\n")
print("ESCOLHA O SEU PROGRAMA *************************")
print("*******************************************")

print("(1) B (2) C")

programa = int(input("Qual o programa?: "))

if(programa == 1):
    print("B")
    b.executar()
elif(programa == 2):
    print("c")
    c.executar()