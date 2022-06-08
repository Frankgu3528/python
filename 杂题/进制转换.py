a,b=input().split("，")
l=len(a)
a=int(a)
b=int(b)
sum=0
while l>=1 :
    t=a//(10**(l-1))
    sum=sum+t*(b**(l-1))
    a=a%(10**(l-1))
    l=l-1
print(sum)
