n=int(input())
list=[]
for i in range(2,n+1):
    import math 
    s=int(math.sqrt(i))
    for j in range(2,s+1):
        if i%j==0:
            break
    else:
        list.append(i)    
print(list)