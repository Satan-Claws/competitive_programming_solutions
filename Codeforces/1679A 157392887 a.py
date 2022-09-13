def msign(x):
    if(x==0):
        return 0
    else:
        return 1

test=int(input())
for t in range(0,test):
    n=int(input())

    if(n%2==1) or (n<4):
        print(-1)
    else:
        x_m=n//4
        x_M=(n//6)+msign(n%6)
        print(x_M,x_m)
