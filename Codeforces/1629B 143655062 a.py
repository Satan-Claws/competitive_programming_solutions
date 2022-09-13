def lr(l,r):
    if(l==1) and (r==1):
        return -1
    elif(l%2==1):
        if(r==l):
            return 0
        elif(r==l+1):
            return 1
        else:
            return 1+((r-l)//2)
    else:
        if(r==l):
            return 0
        else:
            return (r-l+1)//2

t=int(input())
for test in range(0,t):
    l,r,k=map(int,input().strip().split())
    p=lr(l,r)
    if(p==-1):
        print("NO")
    elif(p<=k):
        print("YES")
    else:
        print("NO")
