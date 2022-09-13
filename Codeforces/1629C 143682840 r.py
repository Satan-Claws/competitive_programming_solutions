#1629C
def mex(a):
    temp_a=list(a)
    temp_a.sort()
    c=0
    while c in a:
        c+=1
    return c

def mexify2(a):
    if(len(a)==1):
        return([min(a[0],0),[]])
    else:
        x1=1
        x2=0
        x3=0
        while(x1<len(a)+1):
            x4=mex(a[:x1])
            if(x4>x3):
                x3=x4
                x2=x1
            x1+=1
        return([x3,a[x2:]])
        
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
