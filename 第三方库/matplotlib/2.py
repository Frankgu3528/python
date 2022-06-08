import matplotlib.pyplot as plt
plt.style.use("seaborn")
import numpy as np
fig=plt.figure()
ax=plt.axes()
x=np.linspace(-10,10)
y=np.sin(x)
plt.plot(x,y,color="red",linestyle="-",marker="o",markerfacecolor="blue",linewidth=3.0)
plt.title("sin(x)")
plt.text(0,0,"origin")
plt.show()