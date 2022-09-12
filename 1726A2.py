t=int(input())

for test in range(0,t):
    n=int(input())
    x=list(map(int,input().strip().split()))
    a1=x[0]
    a2=x[n-1]
    m=min(x)
    M=max(x)
    arr=[]
    for i in range(0,n):
        arr.append(x[(i+n-1)%n]-x[i])
    a3=max(arr)

    print(max(M-a1,a2-m,a3))
