a=sorted(dict(counter))[::-1]
b=[i for i in range(len(a))]
c=dict(zip(a,b))
print(c)
