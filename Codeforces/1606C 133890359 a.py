#1606C

t=int(input())
for test in range(0,t):
    n,k=map(int,input().strip().split())
    req=k+1
    target=0
    alpha=list(map(int,input().strip().split()))
    mdp=[]
    for i in range(0,n-1):
        y=alpha[i+1]-alpha[i]
        mdp.append(10**y-1)
    mdp.append(10**10)

    start=0
    while req>0:
        temp_req=req
        dnom=10**alpha[start]
        req=temp_req-min(req,mdp[start])
        target+=min(temp_req,mdp[start])*(dnom)
        start+=1
    print(target)
