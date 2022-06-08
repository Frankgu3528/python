a=[432,32,52,532,632,32]
n=len(a)
for i in range(n):
    #print(i,end=" ")
    for j in range(1,n-i):
        if a[j-1] > a[j] :
            a[j-1],a[j]=a[j],a[j-1]
print(a)