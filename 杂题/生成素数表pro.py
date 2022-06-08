#除了2,3的素数只能是6k+1或6k-1
import math
n=int(input())
primelist=[]
#用来统计满足猜想的素数对个数
count=0
 
#函数用来判断是否为素数
def isprime(n):
    #n为2或3，可以直接判断是素数
    if n == 2 or n == 3:
        return True
    #n可以被2或3整除，可以直接判断不是素数
    if n % 2 == 0 or n % 3 == 0:
        return False
 
    
    #所以2&3以外的素数为6k+1或6k-1的形式，据此可以缩小因子范围
    for k in range(6, int(math.sqrt(n)) + 2, 6):
        if n % (k - 1) == 0 or n % (k + 1) == 0:
            return False
    return True
 
for i in range(2,n+1):
 
    #是素数则添加到素数列表中
    if isprime(i):
        primelist.append(i)
 
#扫描素数列表，判断满足猜想的素数对
for k in range(1,len(primelist)):
    if primelist[k]-primelist[k-1]==2:
        count=count+1
 
#输出满足猜想的素数对的数量
print(count)