#1607E1

t=int(input())
for test in range(0,t):
    n,m=map(int,input().strip().split())
    s=str(input())
    x=[[0,0]]
    size=len(s)
    for i in range(0,size):
        if(s[i]=="L"):
            x.append([x[i][0],x[i][1]-1])
        elif(s[i]=="R"):
            x.append([x[i][0],x[i][1]+1])
        elif(s[i]=="U"):
            x.append([x[i][0]-1,x[i][1]])
        else:
            x.append([x[i][0]+1,x[i][1]])

    ud=[]
    lr=[]
    for i in range(0,size+1):
        ud.append(x[i][0])
        lr.append(x[i][1])


    udi=2
    for i in range(2,size+2):
        ux=min(ud[0:i])
        dx=max(ud[0:i])
        if(dx-ux>=n):
            break
        udi+=1
        
    rli=2
    for i in range(2,size+2):
        lx=min(lr[0:i])
        rx=max(lr[0:i])
        if(rx-lx>=m):
            break
        rli+=1

    i=min(rli,udi)

    lx=-min(lr[0:i-1])
    rx=max(lr[0:i-1])
    ux=-min(ud[0:i-1])
    dx=max(ud[0:i-1])
    print(ux+1,lx+1)
