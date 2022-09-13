#1551A

t=int(input())
for test in range(0,t):
    x=int(input())
    y=x//3
    if(x%3==0):
        print(y,y)
    elif(x%3==1):
        print(y+1,y)
    else:
        print(y,y+1)
