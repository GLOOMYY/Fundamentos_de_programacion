a = int(input())
p = int(input())
q = int(input())
    
x = a
cont = 0
for i in range(p,q+1):
    y = x%(p+cont)
    x = x/(p+cont)
    if (y!=0):
        print(f"{a} no es polifactor entre {p} y {q}")
        exit()
    cont+=1
    
print(f"{a} es polifactor entre {p} y {q}")

