#二分法搜索
a=[1,2,4,5,6,8,9,10,14,252,2154]
x=int(input())
left=0
right=len(a)-1
while left<right :
    mid=(left+right)//2
    if a[mid]<x:
        left=mid+1
    elif a[mid]>x:
        right=mid-1
    elif a[mid]==x:
        break
print("a[%d]=%d"%(mid,x))