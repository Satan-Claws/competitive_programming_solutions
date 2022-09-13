t=int(input())
for test in range(0,t):
    n=int(input())
    x=[n]+[i for i in range(1,n)]
    print(*x)
