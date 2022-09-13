#1712C

T=int(input())
for test in range(0,T):

    n=int(input())
    A=list(map(int,input().strip().split()))
    A.reverse()
    
    delete=[]
    i=0

    while(i<n-1):
        if(A[i]>=A[i+1]):
            i+=1
        else:
            break

    D=A[i+1:]

    if(len(D)>0):
        ind=0
        for i in range(0,n):
            if(A[i] in D):
                ind=i
                break
        
        DD=A[ind:]

        cnt=0
        for item in DD:
            if item not in delete:
                cnt+=1
                delete.append(item)

        print(cnt)
    else:
        print(0)
