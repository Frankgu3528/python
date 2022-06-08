import matplotlib.pyplot as plt

import numpy as np


x=np.linspace(0,10,1000)
plt.plot(x,np.cos(x),"b")
plt.plot(x,np.cos(x)+1,"r")
plt.xlabel("x figure",fontsize=13)
plt.ylabel("y figure")
plt.fill_between(x,np.cos(x),np.cos(x)+1,facecolor="red",alpha=0.3)
plt.vlines(4,np.cos(4),np.cos(4)+1)
plt.show()