from math import sqrt

def lorentz(v):
    c = 299792458
    raiz = round(sqrt(1-(v/c)),15)
    raiz = 1/raiz
    raiz = round(raiz, 15)
    return raiz

def km_a_m(x):
    m = x*0.28
    return m


n = int(input())

lista = []
for i in range(n):
    v = float(input())
    v = km_a_m(v)
    v = lorentz(v)
    lista.append(v)

for i in range(len(lista)):
    print(lista[i])
