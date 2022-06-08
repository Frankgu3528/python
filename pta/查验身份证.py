def isdigit(x):
    flag=True
    for i in range(len(x)):
        if ord("0")>ord(x[i]) or ord(x[i])>ord("9"):
            flag=False
            return  flag
            break
        
n=int(input())
list=[]
for i in range(n):
    list.append(input())
a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
dict={0:"1",1:"0",2:"X",3:"9",4:"8",5:"7",6:"6",7:"5",8:"4",9:"3",10:"2"}
flg=True
for i in range(len(list)):
    s=0
    m=list[i][:len(list[i])-1]
    if isdigit(m) ==False:
        flg=False
        print(list[i])
        continue
    for j in range(len(list[i])-1):
        s=int(list[i][j])*a[j]+s
    # print(s)
    z=s%11
    # print(dict[z])
    # print(list[i][-1])
    if dict[z]!=list[i][-1]:
        flg=False
        print(list[i])
if flg:
    print("All passed")