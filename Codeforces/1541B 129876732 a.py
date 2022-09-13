t=int(input())
for test in range(0,t):
    n=int(input())
    L=list(map(int,input().strip().split()))
    s=0
    k=max(L)
    p=[-1 for i in range(0,k)]
    

    for i in range(0,n):
        pos=L[i]
        p[pos-1]=i+1

    p=[0]+p
    s=0
    for x in range(1,k+1):
        px=p[x]
        y=1
        while(y<=k) and (x*y<=2*n) :
            py=p[y]
            if(py!=-1) and (px!=-1):
                if(py>px):
                    if(x*y==px+py):
                        s+=1
            y+=1
    print(s)
