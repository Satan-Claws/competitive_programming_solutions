#1729D

def target(a,arr):
    if(a==0):
        return []
    else:
        if(sum(arr)<a):
            return [-1]
        else:
            count=0
            temp=0
            for i in range(0,len(arr)):
                temp+=arr[i]
                if(temp<a):
                   count+=1
            if(count==0):
                return [arr[count]]
            else:
                return [arr[count]]+target(a-arr[count],arr[:count])


def make_new(a,arr):
    used=target(a,arr)
    temp=list(arr)
    for i in used:
        temp.pop(temp.index(i))
    return temp

t=int(input())
for test in range(0,t):
    n=int(input())
    x=list(map(int,input().strip().split()))
    y=list(map(int,input().strip().split()))
    pos=[]
    neg=[]
    zer=[]
    for i in range(0,n):
        new=y[i]-x[i]
        if(new>0):
            pos.append(new)
        elif(new==0):
            zer.append(0)
        else:
            neg.append(abs(new))

    pos.sort()
    neg.sort()
    #print(pos,neg,zer)

    temp_pos=list(pos)
    A=[]
    l_neg=len(neg)
    last_index=0
    for i in range(0,l_neg):
        cur=neg[i]
        if(target(cur,pos)==[-1]):
            break
        else:
            x=target(cur,pos)
            last_index+=len(x)
            A.append(x)
            pos=make_new(cur,pos)
            pos.sort()

    len_A=len(A)
    len_pos=len(pos)
    len_zer=len(zer)

    print(len_A+((len_pos+len_zer)//2))


