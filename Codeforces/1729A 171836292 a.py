#1729A

t=int(input())

for test in range(0,t):
    a,b,c=map(int,input().strip().split())
    x=a
    y=abs(b-c)+c
    if(x<y):
        print(1)
    elif(y<x):
        print(2)
    else:
        print(3)
