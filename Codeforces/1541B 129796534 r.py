t=int(input())
for test in range(0,t):
    n=int(input())
    L=list(map(int,input().strip().split()))
    s=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(L[i]*L[j]==i+j+2):
                s+=1
    print(s)
            
