import numpy as np
print(np.arange(2,10,2))#[2 4 6 8]
print(np.ones(10))#[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
print(np.ones((3,3)))
#[[1. 1. 1.]
# [1. 1. 1.]
# [1. 1. 1.]]
a=np.arange(8)
print(np.ones_like(a))#[1 1 1 1 1 1 1 1]仿照a的格式生成一个为1的数组
#同样也有zeros和zeros_like
print(np.full(6,4))#[4 4 4 4 4 4]
print(np.full_like(a,7))#[7 7 7 7 7 7 7 7]
#创建一个内容全为~的数组
print(np.random.randn())#0.33985161465864466
print(np.random.randn(3))#[ 0.94530501 -0.32723138  1.03692599]
print(np.random.randn(3,2))
print(np.random.randn(3,2,4))
#整数随机数
print(np.random.randint(1,100,10))#[68 81 89 11 43 20  6 86 85 68]
#这是1~100之间10个随即整数
print(np.arange(8).reshape(2,4))
#[[0 1 2 3]
# [4 5 6 7]]