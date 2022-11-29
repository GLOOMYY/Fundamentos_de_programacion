

n = int(input())
if (n<1 or n>200):
    exit()
    
m = int(input())
if (m>5000):
    exit()
    
lista = []

for i in range(m):
    x = int(input())
    lista.append(x)

y=0
z=0
lista2=[]
lista.sort()
for i in lista:
    if (i==1):
        lista2.clear()
    x=lista.count(i)
    if (i==0):
        y=i
        lista2.append(lista[i])
    elif x>y:
        lista2.clear()
        lista2.append(x)
        y=x
    elif x==y:
        lista2.append(x)
    
lista2.sort()
# if (lista2[0]==1):
#     print(2)
# else:
print(*lista2, sep = "\n")

# for i in range(len(lista2)):
#     print(lista2[i])
        
    


#print(lista)

# lista.sort()
# print(lista.most_common(1))



# for j in lista:
#     print(j)
#     y = lista.count(j-1)
#     z = lista.count(j)
#     if y<z:
#         print(m,z)
#     elif y>z:
#         print(m-1, y)