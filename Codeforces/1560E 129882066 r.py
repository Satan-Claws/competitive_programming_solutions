def diff(l1,l2):
    s2=len(l2)
    s1=len(l1)
    i=0
    j=0
    while(i<s2) and (j<s1):
        if(l2[i]==l1[j]):
            i+=1
        j+=1
    N=s2
    S=s1
    k=N-i
    return S-N+2*k


def n2l(n):
    b=str(n)
    x=[]
    for i in range(0,len(b)):
        x.append(int(b[i]))
    return x

po=1
up=50
powers=[]
for i in range(0,up):
    powers.append(n2l(po))
    po*=2
print(powers)
def mini(n):
    l1=n2l(n)
    ans=diff(l1,powers[0])
    for i in range(1,up):
        ans=min(ans,diff(l1,powers[i]))
        if(ans==0): break
    return ans

t=int(input())
for i in range(0,t):
    n=int(input())
    print(mini(n))
