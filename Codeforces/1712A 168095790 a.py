#1712A

T=int(input())
for test in range(0,T):
    n,k=map(int,input().strip().split())
    A=list(map(int,input().strip().split()))
    cnt=0
    for i in range(0,k):
        if(A[i]>k):
            cnt+=1

    print(cnt)
