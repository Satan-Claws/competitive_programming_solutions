#1560C

t=int(input())
for test in range(0,t):
    n=int(input())
    s=int((n-1)**(0.5))+1
    c=(s-1)**2+s
    if(n==c):
        print(s,s)
    elif(n<c):
        print(n-(s-1)**2,s)
    else:
        print(s,s**2-n+1)
    
