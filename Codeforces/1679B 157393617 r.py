n,q = map(int,input().strip().split())
L=list(map(int,input().strip().split()))

s=0
for i in range(0,n):
    s+=L[i]

for queries in range(0,q):
    Q=list(map(int,input().strip().split()))
    t=Q[0]
    if(t==1):
        i=Q[1]
        x=Q[2]
        s=s+x-L[i-1]
        L[i-1]=x
    else:
        x=Q[1]
        s=x*n
        L=list([x]*n)
    print(s)
    
