list1=list(map(int,input().split()))
list1=list1[1:]
list2=list(map(int,input().split()))
list2=list2[1:]
newlist=[]
newlist2=[]
for i in list1:
    if i not in list2:
        newlist.append(i)
for i in list2:
    if i not in list1:
        newlist.append(i)
for i in newlist:
    if i not  in newlist2:
        newlist2.append(i)
newlist2=map(str,newlist2)
str=" ".join(newlist2)
print(str)