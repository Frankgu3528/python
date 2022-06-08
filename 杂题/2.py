a,n=input().split()
a=int(a)
n=int(n)
s=0
m=0
for i in range(n) :
    m=a**(i+1)
    s=s+m
print("s =",s)
