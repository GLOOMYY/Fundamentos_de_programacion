n = int(input())
if (n<=9):
    exit()

numero = [int(x) for x in str(n)]
print(str(numero[0])+str(numero[-1]))
