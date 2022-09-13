#1579B

t=int(input())
for test in range(0,t):
    size=int(input())
    a=list(map(int,input().strip().split()))
    x=[]
    for i in range(size):
        for j in range(size-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                x.append([j+1,j+2])
    size2=len(x)
    print(size2)
    for i in range(0,size2):
        print(x[i][0],x[i][1],1)
