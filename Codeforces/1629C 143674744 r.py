#1629C

def mex(a):
    temp_a=list(a)
    temp_a.sort()
    c=0
    while c in a:
        c+=1
    return c

def mexify(a):
    l1=[]
    for i in range(1,len(a)+1):
        l1.append([mex(a[:i]),a[i:]])
    nxt=max(l1)[0]
    j=0
    while l1[j][0]<nxt:
        j+=1
    return l1[j]

t=int(input())
for test in range(0,t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    b=[]
    c=0
    p=mexify(a)
    b.append(p[0])
    c+=1
    while p[1]!=[]:
        p=mexify(p[1])
        b.append(p[0])
        c+=1
    print(c)
    print(*b)
