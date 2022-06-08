m,n=input().split()
m=int(m)
n=int(n)
i=m
sum1=0
while i<=n:
    sum1=sum1+i**2
    i=i+1
j=m
sum2=0
while j<=n:
    sum2=sum2+1/j
    j=j+1
sum=sum1+sum2
str="sum = %.6f"%(sum)
print(str)
