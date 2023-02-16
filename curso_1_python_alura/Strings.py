
v = []
n = int(input("Quantos elementos terá v?"))

for i in range(0,n):
    termo =int(input("qual o termo"))
    v.append(termo)


print(v)
print()
for i in range (0,n):
    print(v[i]," ")
print()
print("(",v[0],v[1],v[2],")")

vs = [1,2,3]
print(vs)
print()

print(vs[0], "teste", vs[1])
