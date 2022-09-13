#1579E1

def prepend(x,q):
    x=[q]+x
    return x

t=int(input())
for test in range(0,t):
    size=int(input())
    p=list(map(int,input().strip().split()))
    z=[p[0]]
    for i in range(1,size):
        if(p[i]>z[0]):
            z.append(p[i])
        else:
            z=prepend(z,p[i])
    print(*z)
