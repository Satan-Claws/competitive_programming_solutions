#1606B

t=int(input())
for test in range(0,t):
    n,k=map(int,input().strip().split())

    L=[1]
    for i in range(1,100):
        L.append(L[i-1]+min(i,k))
    j=0
    while(j>=0):
        if(n<=L[j]):
            print(j)
            j=-1
        else:
            j+=1
