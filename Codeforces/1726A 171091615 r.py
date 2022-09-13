t=int(input())

for test in range(0,t):
    n=int(input())
    x=list(map(int,input().strip().split()))
    m=min(x)
    M=max(x)
    a1=x[0]
    a2=x[n-1]

    #check for cons max
    MList=[i for i,j in enumerate(x) if j==M]
    cons=[]
    for i in range(0,len(MList)):
        y=MList[i]
        mi=(y+1)%n
        if(x[mi]<a1):
            cons.append(M-x[mi])

    #check for fons min
    mList=[i for i,j in enumerate(x) if j==m]
    fons=[]
    for i in range(0,len(mList)):
        y=mList[i]
        mi=(y-1)%n
        if(x[mi]>a2):
            fons.append(x[mi]-m)

    if(len(cons)>0):
        if(len(fons)>0):
            print(max(a2-m,M-a1,max(cons),max(fons)))
        else:
            print(max(a2-m,M-a1,max(cons)))
    else:
        if(len(fons)>0):
            print(max(a2-m,M-a1,max(fons)))
        else:
            print(max(a2-m,M-a1))
