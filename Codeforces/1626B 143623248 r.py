#1626B

t=int(input())
for test in range(0,t):
    num=str(input())
    x=[]
    for i in range(0,len(num)-1):
        x.append(int(num[:i]+str(int(num[i])+int(num[i+1]))+num[i+2:]))
    print(max(x))
        
