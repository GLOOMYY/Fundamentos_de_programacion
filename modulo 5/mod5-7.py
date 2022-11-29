def area_cuadrado(lado):
    area = lado*lado
    return area


lotes = int(input())
lado = float(input())
incremento = float(input())

area_tot = 0
for i in range(lotes):
    x = area_cuadrado(lado)
    area_tot+=x
    lado+=incremento
    
print(f"El area total es de {area_tot} metros cuadrados")