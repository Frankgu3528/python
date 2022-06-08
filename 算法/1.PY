import matplotlib.pyplot as plt
import numpy as np
data = np.array([0,0,10,135.5,30,112.5,30,87.5,
    50,112.5,50,87.5,50,37.5,110,62.5,
    190,62.5,190,162.5,190,187.5]).reshape(11,2)
fig,ax=plt.subplots()
x = data[:,0]
y = data[:,1]
plt.xlim(0,300)
plt.ylim(0,200)
plt.xticks([0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300])
plt.yticks([0,25,50,75,100,125,150,175,200])
ax.scatter(x, y,linewidths=0.1)
plt.grid()
plt.show()