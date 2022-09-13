#1726B


t=int(input())

for test in range(0,t):
    n,m=map(int,input().strip().split())
    if(n>m):
        print("No")
    else:
        k1=m-n
        k2=k1//2
        if((n-1)%2==0):
            print("Yes")
            for i in range(0,n):
                if(i<n-1):
                    print(1,end=" ")
                else:
                    print(1+k1)
        else:
            if(m%2==0):
                print("Yes")
                for i in range(0,n):
                    if(i<n-2):
                        print(1,end=" ")
                    else:
                        print(1+k2,end=" ")
            else:
                if(n==1):
                    print("Yes")
                    print(m)
                else:
                    print("No")
