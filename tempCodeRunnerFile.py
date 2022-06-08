n=int(input())
for i in range(n):
    t=int(input())
    lst=[]
    s1=0
    s2=0
    for i in range(t):
        lst.append(list(map(int,input().split())))
    # print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i > j:
                s1+=lst[i][j]
            if i < j:
                s2+=lst[i][j]
    if s1 == 0 and s2 != 0:
        print("lower triangular matrix")
    elif s1 != 0 and s2 == 0:
        print("upper triangular matrix")
    else:
        print("no")
