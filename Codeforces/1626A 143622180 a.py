t=int(input())
for test in range(0,t):
    word=str(input())
    double=""
    notd=""
    size=len(word)
    for i in range(0,size-1):
        y=word[i]
        if(y in word[i+1:]):
            double+=y
    for i in word:
        if(i not in double):
            notd+=i

    print(double+double+notd)
