from math import sqrt, pow

def par(x):
    x = int(x)
    x = 4+x
    x = 5*(pow(x,3))
    fog = sqrt(2+x)
    return fog

def impar(x):
    x = int(x)
    x = 2+5*(x)
    x = 4+sqrt(x)
    gof = pow(x,3)
    return gof

x = int(input())
lista = []
lista.append(x)

while True:
    x = int(input())
    if (x==0):
        break
    else:
        lista.append(x)

for i in range(len(lista)):
    if (lista[i]%2==0):
        x = lista[i]
        x = par(x)
        print(x)	
    elif (lista[i]%2!=0):        
        x = lista[i]
        x = impar(x)
        print(x)