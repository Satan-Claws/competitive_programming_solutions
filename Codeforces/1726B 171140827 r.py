#1726B
import sys

t=int(input())

for test in range(0,t):
    n,m=map(int,input().strip().split())
    if(n>m):
        sys.stdout.write("No"+"\n")
    else:
        k1=m-n
        k2=k1//2
        if(n%2==1):
            sys.stdout.write("Yes"+"\n")
            for i in range(0,n):
                if(i<n-1):
                    sys.stdout.write("1 ")
                else:
                    sys.stdout.write(str(1+k1)+"\n")
        else:
            if(m%2==0):
                sys.stdout.write("Yes"+"\n")
                for i in range(0,n):
                    if(i<n-2):
                        sys.stdout.write("1 ")
                    elif(i==n-2):
                        sys.stdout.write(str(1+k2)+" ")
                    else:
                        sys.stdout.write(str(1+k2)+"\n")
            else:
                if(n==1):
                    sys.stdout.write("Yes"+"\n")
                    sys.stdout.write(str(m)+"\n")
                else:
                    sys.stdout.write("No"+"\n")
