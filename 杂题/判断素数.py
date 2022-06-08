n=int(input())
import math 
s=int(math.sqrt(n))
for i in range(1,s+1):
    if n%2 == 0 :
        print ("bushi")
        break
    else:
        print("shide")
        break
        