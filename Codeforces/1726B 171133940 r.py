#1726B


t=int(input())

for test in range(0,t):
    n,m=map(int,input().strip().split())
    if(n>m):
        print("No")
    else:
        if((n-1)%2==0):
            x=[1 for i in range(0,n)]
            x[n-1]+=(m-n)
            print("Yes")
            print(*x)
        else:
            if(m%2==0):
                x=[1 for i in range(0,n)]
                x[n-2]+=(m-n)//2
                x[n-1]+=(m-n)//2
                print("Yes")
                print(*x)
            else:
                if(n==1):
                    print("Yes")
                    print(m)
                else:
                    print("No")
