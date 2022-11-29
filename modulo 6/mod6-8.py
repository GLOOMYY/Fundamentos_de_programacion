def fichas_disponibles(n):
    cont1 = n-1
    lista_fichas = []
    while (cont1!=0):
        x = int(input())
        lista_fichas.append(x)
        cont1-=1
    return lista_fichas

def fichas_totales(n):
    lista_todas = []
    for i in range(n+1):
        lista_todas.append(i)
    if 0 in lista_todas:
        lista_todas.pop(0)
    return lista_todas


n = int(input())
if (n<4 or n>10000):
     exit()

lista_disponibles = fichas_disponibles(n)
lista_totales = fichas_totales(n)

suma_disponibles = sum(lista_disponibles)
suma_totales = sum(lista_totales)

falta = suma_totales - suma_disponibles

print(f"La ficha faltante es la {falta}")