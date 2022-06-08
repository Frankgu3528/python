def isprime(n):
    if n<=1:
        isprime=False
    else:
        isprime=True
    import math 
    s=int(math.sqrt(n))
    if n>=4:
        for i in range(2,s+1):
            if n%i==0:
                isprime=False
                break
    return isprime
