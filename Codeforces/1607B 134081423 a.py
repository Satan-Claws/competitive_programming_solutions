#1607B

def md(n):
    if(n%4==1):
        return -n
    elif(n%4==2):
        return 1
    elif(n%4==3):
        return n+1
    else:
        return 0

def grass(pos,step):
    if(pos%2==0):
        return pos+md(step)
    else:
        return pos-md(step)

t=int(input())
for test in range(0,t):
    x,n=map(int,input().strip().split())
    print(grass(x,n))
