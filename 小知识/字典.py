a=["吕布","关羽"]
b=["口口步","关习习"]
zidian=dict(zip(a,b))
#zidian.pop("关羽")
#print(zidian) 输出{'吕布': '口口步'}

#zidian["刘备"]="刘baby"
#print(zidian) 输出{'吕布': '口口步', '关羽': '关习习', '刘备': '刘baby'}

d=dict.fromkeys("fishc",100)
d["f"]=115
print(d) #输出{'f': 100, 'i': 100, 's': 100, 'h': 100, 'c': 100}

#s=d.values()键的序列
#print(s) 
#s=d.values()值的序列
#print(s) 