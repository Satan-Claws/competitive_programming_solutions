#1629C
def mex(a):
    a=set(a)
    c=0
    while c in a:
        c+=1
    return c
 
def mexify2(a):
    if(len(a)==1):
        return([mex(a),[]])
    else:
        x1=1
        ind=0
        maxmex=0
        while(x1<len(a)+1):
            curmex=mex(a[:x1])
            if(curmex>maxmex):
                maxmex=curmex
                ind=x1
            x1+=1
        return([maxmex,a[ind:]])
        
t=int(input())
for test in range(0,t):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[]
    c=0
    p=mexify2(a)
    b.append(p[0])
    c+=1
    while p[1]!=[]:
        p=mexify2(p[1])
        b.append(p[0])
        c+=1
    print(c)
    print(*b)
