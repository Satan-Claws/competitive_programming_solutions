t=int(input())
for test in range(0,t):
    n=int(input())
    x=[]
    if(n%2==0):
        for i in range(0,n//2):
            x.append(2*i+2)
            x.append(2*i+1)
    else:
        if(n==3):
            x=[3,1,2]
        else:
            m=n-3
            for i in range(0,m//2):
                x.append(2*i+2)
                x.append(2*
                         i+1)
            x.append(n)
            x.append(n-2)
            x.append(n-1)
    print(x)
