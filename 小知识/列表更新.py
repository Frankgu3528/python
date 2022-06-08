list=[1,2,3,4,5]
for i in list:
    i=i+1
print(list)
#输出依然是[1, 2, 3, 4, 5]！这样列表是不会更新的！
for i in range(len(list)):
    list[i]+=1
print(list)
#这次的输出变成了[2, 3, 4, 5, 6]，要用下标索引才行！