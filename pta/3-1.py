list=list(map(int,input().split()))
average=sum(list)/len(list)
for i in range(len(list)):
    if list[i] > average :
        print(list[i],end=" ")