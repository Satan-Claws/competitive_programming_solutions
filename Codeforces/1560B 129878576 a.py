#1560B

t=int(input())
for test in range(0,t):
    a,b,c=map(int,input().split())
    diff=abs(b-a)
    size=2*diff
    if(max(a,b,c)>size) :
        print(-1)
    else:
        p=1+diff
        if(c==p):
            print(1)
        elif(c<p):
            print(c+diff)
        else:
            print(c-diff)
    
