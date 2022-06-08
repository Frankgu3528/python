a,b=input().split()
a=int(a)
b=int(b)
if a<=b<=100 :
    print("fahr celsius")
    i=a
    while i<=b:
        j=5*(i-32)/9
        j=round(j,1)
        print(i,"  ",j,end=" ")
        i+=2
        print( )
else:
    print("Invalid.")