#1579
def cycle(x,l,r,d):
    if(d==0):
        return x
    else:
        y=x[l-1:r]
        s=len(y)
        y=y+y
        y=y[d:d+s]
        y=x[:l-1]+y+x[r:]
        return y

t=int(input())
for test in range(0,t):
    size=int(input())
    no=list(map(int,input().strip().split()))
    x=[]
    s=0
    on=list(no)
    on.sort()
    for i in range(0,size):
        newmin=on[i]
        non=no[i:]
        y=i+non.index(newmin)
        if(y!=i):
            no=cycle(no,i+1,size,y-i)
            s+=1
            x.append([i+1,size,y-i])

    print(s)
    if(s>0):
        for i in range(0,s):
            z=x[i]
            print(*z)
