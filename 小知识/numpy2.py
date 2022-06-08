import numpy as np
x=np.arange(20).reshape(4,5)
print(x)
#[[ 0  1  2  3  4] 
# [ 5  6  7  8  9] 
# [10 11 12 13 14] 
# [15 16 17 18 19]]
print(x[1,1])#输出6
print(x[2,0])#输出10
#省略一个索引，输出降低一个维度的数组
print(x[1])#[5 6 7 8 9]
print(x[3])#[15 16 17 18 19]
print(x[-1])#[15 16 17 18 19]
print(x[:-1])#类似于切片
#[[ 0  1  2  3  4]
# [ 5  6  7  8  9]
# [10 11 12 13 14]]
print(x[:2,:2])
#[[0 1]
# [5 6]]
print(x[:,2])#[ 2  7 12 17]获得一列
#切片的修改会改变原来的数组
x[:,2]=0
print(x)
x=np.arange(20).reshape(4,5)
print(x[[0,2]])#切第一行，第三行
#[[ 0  1  2  3  4]
# [10 11 12 13 14]]
print(x[:,[0,2]])#切第一列，第三列
#布尔索引
a=np.arange(10)#[0 1 2 3 4 5 6 7 8 9]
print(a>5)#[False False False False False False  True  True  True  True]
print(a[a>5])#[6 7 8 9]
a[a<=5]=0;a[a>5]=1
print(a)#[0 0 0 0 0 0 1 1 1 1]
#条件还能组合

