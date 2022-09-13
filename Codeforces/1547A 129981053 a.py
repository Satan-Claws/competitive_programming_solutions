#1547A
t=int(input())
for test in range(0,t):
    space=str(input())
    a1,b1=map(int,input().strip().split())
    a2,b2=map(int,input().strip().split())
    a3,b3=map(int,input().strip().split())

    if(a1==a2) and (b1!=b2):
        if(a3==a1):
            if(b3<max(b1,b2)) and (b3>min(b1,b2)):
                print(2+abs(b2-b1))
            else:
                print(abs(b2-b1))
        else:
            print(abs(b2-b1))

    elif(b1==b2) and (a1!=a2):
        if(b3==b1):
            if(a3<max(a1,a2)) and (a3>min(a1,a2)):
                print(2+abs(a2-a1))
            else:
                print(abs(a2-a1))
        else:
            print(abs(a2-a1))

    elif(a1==a2) and (b1==b2):
        print(0)

    else:
        print(abs(a1-a2)+abs(b1-b2))
            
            
        
