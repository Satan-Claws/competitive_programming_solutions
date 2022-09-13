#1560A
t=int(input())
X=[]
for i in range(1,31):
    if(i%3!=0) and (i%10!=3):
        X.append(i)
for test in range(0,t):
    n=int(input())
    d=(n-1)//18
    r=n-18*d
    if(r==0): r=18
    print(X[r-1]+30*d)
