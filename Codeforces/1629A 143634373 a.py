#1629A
t=int(input())

for test in range(0,t):
    n,k=map(int,input().strip().split())
    l1=list(map(int,input().strip().split()))
    l2=list(map(int,input().strip().split()))
    l=[]
    for i in range(0,n):
        l.append([l1[i],l2[i]])

    l.sort()

    for i in range(0,n):
        if(k>=l[i][0]):
            k+=l[i][1]
        else:
            break
    print(k)
