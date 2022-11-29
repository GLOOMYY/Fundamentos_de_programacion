

def separar_numeros(n):
    numero = [int(x) for x in str(n)]
    return numero

def hyperpar(x):
    lista = separar_numeros(x)
    for i in range(len(lista)):
        if (lista[i]%2==0):
            print("Hyperpar")
        else:
            print("No es hyperpar")

lista = []

while True:
    x = int(input())
    if (x==-1):
        break
    else:
        lista.append(x)

print(lista)

for i in range(len(lista)):
    print(hyperpar(lista[i]))