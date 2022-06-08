import numpy as np
import matplotlib.pyplot as plt

X=np.random.normal(0,1,1000)
Y=np.random.normal(0,1,1000)
T=np.arctan2(Y,X)#用来控制颜色的一个量
plt.scatter(X,Y,s=75,c=T,alpha=0.5)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.show()