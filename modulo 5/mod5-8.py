capacidad = float(input())
if (capacidad<0):
    exit()
    
cantidad = int(input())

tel = 0
for i in range(cantidad):
    elef = float(input())
    capacidad-=elef
    if (capacidad>=0):
        tel+=1
    
print(tel)