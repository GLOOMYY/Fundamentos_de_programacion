lista = []

while True:
    n = int(input())
    if n==0:
        break
    else:
        lista.append(n)

y=0
cont=0
x=0
for i in range(len(lista)):
    x = lista[i]
    for j in range(len(lista)):
        y=x+lista[j]
        if (y==1995):
            cont+=1
    

print(int(cont/2))

    