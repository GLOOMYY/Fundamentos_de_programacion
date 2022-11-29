x = float(input())
if (x<10):
    exit()

cont = 0
while True:
    if (x>10):
        x/=2
        cont+=1
    else:
        break
    
print(cont)