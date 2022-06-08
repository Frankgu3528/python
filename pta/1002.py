n=int(input())
l=len(str(n))
sum=0
for i in range(l-1,-1,-1):
    a=n//(10**i)
    n=n%(10**i)
    sum=sum+a
#由此得到各位数字之和sum
zidian=dict(zip([1,2,3,4,5,6,7,8,9,0],["yi","er","san","si","wu","liu","qi","ba","jiu","ling"]))
l=len(str(sum))
#print(l)
str=""
for j in range(l-1,-1,-1):
    a=sum//(10**j)
    sum=sum%(10**j)
    str=str+zidian[a]+" "
print(str.rstrip())


