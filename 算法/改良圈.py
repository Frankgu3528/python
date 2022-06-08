import numpy as np
import matplotlib.pyplot as plt
# 输入数据
data = np.array([10,135.5,30,112.5,30,87.5,
    50,112.5,50,87.5,50,37.5,110,62.5,
    190,62.5,190,162.5,190,187.5]).reshape(10,2)


    
# 定义距离
def distance(data1,data2):
	return np.sqrt((data1[0]-data2[0])**2+(data1[1]-data2[1])**2)

# 改良圈
for m in np.arange(1,len(data)-3):
    for n in np.arange(m+1,len(data)-2):
        if distance(data[m],data[n])+distance(data[m+1],data[n+1])-distance(data[m],data[m+1])-distance(data[n],data[n+1]):
            data[m+1:n+1]=data[n:m:-1] #当距离变短时交换位置
        else:
            continue
X=[];Y=[]

for xnew,ynew in data:
    X.append(xnew)
    Y.append(ynew)
plt.plot(X,Y) #改良圈算法后的巡航路线
plt.show()

    