#1538B

t=int(input())
for test in range(0,t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    s=0
    for i in range(0,n):
        s+=l[i]
    if(s%n!=0):
        print(-1)
    else:
        k=0
        avg=s//n
        for i in range(0,n):
            if(l[i]>avg):
                k+=1
        print(k)
