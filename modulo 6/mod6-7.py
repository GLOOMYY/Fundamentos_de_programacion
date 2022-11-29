#  La entrada contiene una serie de líneas (más de 1 y no más de 500), con el valor
# correspondiente de N (1 ≤ N ≤ 10000) y termina con un valor de 0 que no corresponde a
# un N.

while True:
    n = int(input())
    if (n>10000 or n<1 or n==0):
        break
    x=1
    while True:
        n=n-x
        x+=1
        if (n==0):
            print("Puede ser un racimo ideal")
            break
        elif (n<0):
            print("No puede ser un racimo ideal")
            break
            
            
