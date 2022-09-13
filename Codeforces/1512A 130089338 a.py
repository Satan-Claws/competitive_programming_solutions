#1512A
t=int(input())

for test in range(0,t):
    n=int(input())
    L=list(map(int,input().strip().split()))
    a=L[0]
    b=L[1]
    c=L[2]
    if(a==b) and (b==c):
        s=a
    elif(a==b) and (b!=c):
        s=a
    elif(a==c) and (b!=a):
        s=a
    else:
        s=b
    for i in range(0,n):
        if(L[i]!=s):
            print(i+1)
