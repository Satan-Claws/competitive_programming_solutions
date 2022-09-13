#1547B
abcd="abcdefghijklmnopqrstuvwxyz"


def alpha(x,i):
    if(x=="a") and (i==1):
        print("YES")
    else:
        if(x[0]==abcd[i-1]):
            return alpha(x[1:],i-1)
        elif(x[i-1]==abcd[i-1]):
            return alpha(x[:-1],i-1)
        else:
            print("NO")

t=int(input())
for test in range(0,t):
    y=str(input())
    z=len(y)
    alpha(y,z)
