#1607C

t=int(input())
for test in range(0,t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    dist=a
    dist.sort()
    size=len(dist)
    x=[dist[0]]
    for i in range(0,size-1):
        x.append(dist[i+1]-dist[i])
    print(max(x))
