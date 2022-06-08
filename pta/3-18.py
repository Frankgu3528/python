str=input()
list=list(str)
newlist1=[]
newlist2=[]
newlist3=[]
for i in list:
    if ord("a")<=ord(i)<=ord("z") or   ord("A")<=ord(i)<=ord("Z") :
        newlist1.append(i)
for i in newlist1:
    if i not in newlist2:
        newlist2.append(i)
#print(len(newlist2))
for i in range(len(newlist2)-1):
    for j in range(i+1,len(newlist2)):
         if ord(newlist2[i])==ord(newlist2[j])+32 or ord(newlist2[i])==ord(newlist2[j])-32 :
            newlist2[j]=newlist2[i]#直接删掉那个会导致下标不对，先让他们一样，在进行查重去掉
for i in newlist2:
    if i not in newlist3:
        newlist3.append(i)


if len(newlist3)<10:
    print("not found")
else:
    newlist3=newlist3[0:10]
    print("".join(newlist3))
