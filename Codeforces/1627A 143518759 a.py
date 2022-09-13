t=int(input())
for test in range(0,t):
    n,m,r,c=map(int,input().strip().split())
    x=[]
    c_w=""
    col_w=""
    for i in range(0,n):
        y=str(input())
        x.append(y)
        c_w+=y
        col_w+=y[c-1]

    if "B" in c_w:
        if x[r-1][c-1]=="B":
            print(0)
        elif "B" in col_w:
            print(1)
        elif "B" in x[r-1]:
            print(1)
        else:
            print(2)

    else:
        print(-1)
