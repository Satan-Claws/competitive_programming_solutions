#1712B

T=int(input())

for test in range(0,T):
    n=int(input())
    L=[n-i for i in range(0,n)]

    for i in range(0,n//2):
        L[2*i],L[2*i+1]=L[2*i+1],L[2*i]

    L.reverse()
    print(*L)
