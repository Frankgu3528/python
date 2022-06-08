n=int(input())
if n<10:
    for i in range(1,n+1):
        print(i,end="")
if  10<=n<100:
    a1=n//10;a2=n%10
    str1="S"*a1
    list=list(x for x in range(1,a2+1))
    list=map(str,list)
    str2="".join(list)
    print(str1+str2)
if 100<=n<1000:
    a1=n//100;a2=(n%100)//10;a3=n%10
    str1="B"*a1
    str2="S"*a2
    list=list(x for x in range(1,a3+1))
    list=map(str,list)
    str3="".join(list)
    print(str1+str2+str3)