def funcion(x):
    if (x%123==0):
        y = 0
    else:
        y = 1+(funcion(x+23))
    return y
        
cont = int(input())
lista = []

for i in range(cont):
    x = int(input())
    lista.append(x)
    
for i in range(len(lista)):
    print(funcion(lista[i]))