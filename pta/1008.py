n,m=input().split()
n=int(n)
m=int(m)
list=list(map(int,input().split()))
#切片操作基本表达式：object[start_index:end_index:step]
m=m%n
new1=list[n-m:n]
new2=list[:n-m]
new=new1+new2
new=map(str,new)
print(" ".join(new))

