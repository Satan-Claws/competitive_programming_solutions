#1729B

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
    "j":"100",
    "k":"110",
    "l":"120",
    "m":"130",
    "n":"140",
    "o":"150",
    "p":"160",
    "q":"170",
    "r":"180",
    "s":"190",
    "t":"200",
    "u":"210",
    "v":"220",
    "w":"230",
    "x":"240",
    "y":"250",
    "z":"260"
    }

reverse_encoding ={v: k for k,v in encoding.items()}

t=int(input())

for test in range(0,t):
    n=int(input())
    s=str(input())
    tr=""
    A=[]
    i=len(s)-1
    while i>=0:
        out=""
        if(s[i]=="0"):
            out=s[i-2]+s[i-1]+s[i]
            i=i-3
        else:
            out=s[i]
            i=i-1
        A.append(out)
    A.reverse()
    #print(A)
    for i in range(0,len(A)):
        tr+=reverse_encoding[A[i]]
    print(tr)

