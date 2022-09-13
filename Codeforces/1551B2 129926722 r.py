#1551B2
t=int(input())
for test in range(0,t):
    n,k=map(int,input().strip().split())
    a=list(map(int,input().strip().split()))
    x=[0 for i in range(0,n)]
    y=[]
    for i in range(0,n):
        p=a[i]
        q=x[p-1]+1
        if(q>k): q=0
        y.append(q)
        x[p-1]+=1

    print(y)
        
