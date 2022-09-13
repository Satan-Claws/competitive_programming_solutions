#1729C

encoding={
    "a":"1",
    "b":"2",
    "c":"3",
    "d":"4",
    "e":"5",
    "f":"6",
    "g":"7",
    "h":"8",
    "i":"9",
    "j":"10",
    "k":"11",
    "l":"12",
    "m":"13",
    "n":"14",
    "o":"15",
    "p":"16",
    "q":"17",
    "r":"18",
    "s":"19",
    "t":"20",
    "u":"21",
    "v":"22",
    "w":"23",
    "x":"24",
    "y":"25",
    "z":"26"
    }


t=int(input())
for test in range(0,t):
    s=str(input())
    A=[]
    B=[]
    for i in range(0,len(s)):
        A.append([int(encoding[s[i]]),i])
        B.append(A[i][0])
    first=A[0][0]
    last=A[-1][0]

    out=[]
    if(first>last):
        mid=A[1:-1]
        mid.sort()
        mid.reverse()
        new=[A[0]]+mid+[A[-1]]
        for i in range(0,len(B)):
            if(new[i][0]<=first) and (new[i][0]>=last):
                out.append(1+new[i][1])

    else:
        mid=A[1:-1]
        mid.sort()
        new=[A[0]]+mid+[A[-1]]
        for i in range(0,len(B)):
            if(new[i][0]>=first) and (new[i][0]<=last):
                out.append(1+new[i][1])
    print(abs(first-last),len(out))            
    print(*out)
