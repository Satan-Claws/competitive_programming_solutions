#1712C


#i did for non-increasing like a retard
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

    j=i+1
    while(j<n):
        curr=A[j]
        if curr not in delete:
            delete.append(curr)   
        j+=1
        

    for i in range(1,n):
        if(A[i-1] in delete):
            if(A[i] not in delete):
                delete.append(A[i])

    print(len(delete))
