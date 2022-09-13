def dec2bin(x):
    t=[]
    if(x==0):
        t=[0]
    else:
        while(x>0):
            t.append(x%2)
            x=x//2
        t.reverse()
    return t

def bin2dec(x):
    r=1
    s=0
    x.reverse()
    if(x==[0]):
        return 0
    else:
        while(len(x)>0):
            p=x.pop(0)
            s+=r*p
            r*=2
        return s
        

def yy(x1,y1,x2):
    a=x1^y1
    aa=dec2bin(a)
    xx=dec2bin(x2)
    za=len(aa)
    zx=len(xx)
    zy=2+max(za,zx)
    new_a=[0 for i in range(zy-za)]+aa
    new_x=[0 for i in range(zy-zx)]+xx
    for i in range(0,zy):
        if(new_a[i]==0):
            if(new_x[i]==1):
                new_a[i]=1
    a_star=bin2dec(new_a)
    y2=x2^a_star
    return y2

t=int(input())
for test in range(0,t):
    n=int(input())
    x=list(map(int,input().strip().split()))
    y=[0]
    for i in range(0,n-1):
        y.append(yy(x[i],y[i],x[i+1]))
    print(*y)
