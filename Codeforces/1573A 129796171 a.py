t=int(input())
def contri(n):
    if(n>0):
        return n+1
    else:
        return 0
for test in range(0,t):
    size=int(input())
    x=str(input())
    s=0
    for i in range(0,size-1):
        s+=contri(int(x[i]))
    s+=int(x[-1])
    print(s)
        
    
