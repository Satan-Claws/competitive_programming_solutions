#1607C

t=int(input())
for test in range(0,t):
    n=int(input())
    dist=[]
    a=list(map(int,input().strip().split()))
    for i in range(0,n):
        if(a[i] not in dist):
            dist.append(a[i])
    dist.sort()
    size=len(dist)
    x=[dist[0]]
    for i in range(0,size-1):
        x.append(dist[i+1]-dist[i])
    print(max(x))
