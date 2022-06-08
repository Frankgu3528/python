from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure()
ax=plt.axes(projection="3d")
x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
X,Y=np.meshgrid(x,y)
Z=np.sqrt(0.2*X**2-0.1*Y**2)+4
ax.plot_surface(X,Y,Z,rstride=1, cstride=1,cmap='rainbow',edgecolor='none')
plt.show()
