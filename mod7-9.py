def primer(n):
    return n+1

def segundo(m):
    return a(m-1,1)

def tercer(m, n):
    return a(m-1, a(m,n-1))
    
def a(m,n):
    if (m==0):
        return primer(n)
    elif (m>0 and n==0):
        return segundo(m)
    elif (m>0 and n>0):
        return tercer(m, n)
     

    
cont = int(input())
m=[]
n=[]

for i in range(cont):
    x = int(input())
    m.append(x)
    y = int(input())
    n.append(y)
    
for i in range(len(m)):
    print(a(m[i],n[i]))