#1606A


t=int(input())

for test in range(0,t):
    s=str(input())
    size=len(s)
    if(size==1):
        print(s)
    elif(size==2):
        if(s=="ab") or (s=="ba"):
            print("aa")
        else:
            print(s)
    else:
        ab=0
        ba=0
        for i in range(0,len(s)-1):
            if(s[i:i+2]=="ab"):
                ab+=1
            elif(s[i:i+2]=="ba"):
                ba+=1
        if(ab!=ba):
            s=s
            if(s[0]=="a"):
                s="b"+s[1:]
            else:
                s="a"+s[1:]
        print(s)
