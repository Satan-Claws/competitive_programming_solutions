#1607A

cases=int(input())
for test in range(0,cases):
    letters=str(input())
    s=str(input())
    size=len(s)
    t=[]
    for i in range(0,size):
        for j in range(0,26):
            if(s[i]==letters[j]):
                t.append(j+1)

    su=0
    if(size>1):
        for i in range(0,size-1):
            su+=abs(t[i+1]-t[i])
    print(su)

        
