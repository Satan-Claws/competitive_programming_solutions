#1579A

t=int(input())
for test in range(0,t):
    s=str(input())
    a=0
    b=0
    c=0
    size=len(s)
    for i in range(0,size):
        if(s[i]=="A"):
            a+=1
        elif(s[i]=="B"):
            b+=1
        else:
            c+=1
    if(a+c==b):
        print("YES")
    else:
        print("NO")
