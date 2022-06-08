a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a>b :
    a,b=b,a
if b>c :
    b,c=c,b
if a>b:
    a,b=b,a
str="%d->%d->%d"%(a,b,c)
print(str)
