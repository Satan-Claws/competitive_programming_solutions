#1573B

t=int(input())
for test in range(0,t):    
    size=int(input())
    a=list(map(int,input().strip().split()))
    b=list(map(int,input().strip().split()))

    pa=[0 for i in range(0,size)]
    pb=[0 for i in range(0,size)]

    for i in range(0,size):
        xa=a[i]
        xa=(xa-1)//2
        pa[xa]=i
        xb=b[i]
        xb=(xb-1)//2
        pb[xb]=i
    
    m=0
    k=pa[0]
    for i in range(0,size-1):
        m=min(pb[i+1:])
        k=min(k,m+pa[i+1])
    print(k)
        
