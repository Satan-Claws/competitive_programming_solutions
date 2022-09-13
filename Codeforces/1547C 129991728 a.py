#1547C

t=int(input())


for test in range(0,t):
    def a2b():
        if(len(a1)>0):
            while(a1[0]<=k1[0]):
                y1a=a1.pop(0)
                if(y1a==0):
                    k1[0]+=1
                    x1.append(0)
                else:
                    x1.append(y1a)
                if(len(a1)==0):
                    break
        if(len(b1)>0):
            while(b1[0]<=k1[0]):
                y1b=b1.pop(0)
                if(y1b==0):
                    k1[0]+=1
                    x1.append(0)
                else:
                    x1.append(y1b)
                if(len(b1)==0):
                    break
    space=str(input())
    k,m,n=map(int,input().strip().split())
    k1=[k]
    a1=list(map(int,input().strip().split()))
    b1=list(map(int,input().strip().split()))
    x1=[]

                
    for i in range(0,n+m):
        a2b()
    if(len(x1)==n+m):
        print(*x1)
    else:
        print(-1)
