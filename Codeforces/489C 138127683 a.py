m,s=map(int,input().strip().split())
#if it exists
def largest(x,y):
    ans=""
    size=0
    while(size<y):
        if(x>=9):
            ans+="9"
            x-=9
            size+=1
        else:
            ans+=str(x)
            x=0
            size+=1
    return ans

if(s>m*9):
    print(-1,-1)
elif(s==0):
    if(m==1):
        print(0,0)
    else:
        print(-1,-1)
else:
    lans=largest(s,m)
    if(lans[-1]=="0"):
        sans=largest(s-1,m-1)
        sans+="1"
        sans=sans[::-1]
    else:
        sans=lans
        sans=sans[::-1]

    print(int(sans),int(lans))
            
    
    
