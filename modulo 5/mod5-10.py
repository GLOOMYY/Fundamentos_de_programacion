def posicion(x):
    if (x%2==0):
        y = x//2
        z = (x//2)-1
    else:
        y = (x//2)+1
        z = x//2
    return y

def bandera(l, h, pos_x, pos_y):
    x = "0"*(l-pos_x)
    y = "+"
    for i in range(h - pos_y):
        print(f"{x}{y}{x}")
    
    print("+"*l)
    
    for i in range(h - pos_y):
        print(f"{x}{y}{x}")
    

l = int(input()) #largo
h = int(input()) #altura

pos_x = posicion(l)
pos_y = posicion(h)

bandera(l, h, pos_x, pos_y)