from math import pow, sqrt

def p(x):
    x = float(x)
    y = (2*x)+1
    return y

def a(x):
    x = float(x)
    y = pow(3,x)
    return y

def n(x):
    x = float(x)
    y = sqrt((5*x)+4)
    return y

def compuesta(x):
    x = float(x)
    return p(a(n(x)))

cont = int(input())
lista = []

for i in range(cont):
    x = float(input())
    lista.append(x)
    
for j in range(len(lista)):
    print(compuesta(lista[j]))
