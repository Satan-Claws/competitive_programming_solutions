#1538A

t=int(input())
for test in range(0,t):
    size=int(input())
    a=list(map(int,input().strip().split()))
    xl=1+a.index(min(a))
    yl=1+a.index(max(a))
    xr=size+1-xl
    yr=size+1-yl
    middle=(1+size)/2

    if(xl<=middle) and (yl<=middle):
        print(max(xl,yl))
    elif(xr<=middle) and (yr<=middle):
        print(max(xr,yr))
    elif(xl<=middle) and (yr<=middle):
        print(min(xl+yr,yl,xr))
    elif(xr<=middle) and (yl<=middle):
        print(min(xr+yl,yr,xl))
