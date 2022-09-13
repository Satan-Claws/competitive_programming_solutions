t=int(input())

for test in range(0,t):
    n=int(input())
    x=list(map(int,input().strip().split()))
    m=min(x)
    M=max(x)
    a1=x[0]
    a2=x[n-1]
    MList=[i for i,j in enumerate(x) if j==M]
    cons=[]
    for i in range(0,len(MList)):
        y=MList[i]
        mi=(y+1)%n
        if(x[mi]<a1):
            cons.append(M-x[mi])
    if len(cons)>0:
        a3=max(cons)
        print(max(M-a1,a2-m,a3))
    else:
        print(max(M-a1,a2-m))
