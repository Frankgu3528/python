from random import choice
import matplotlib.pyplot as plt
class randomwalk():
    def __init__(self,num_points=50000):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_direction=choice([1, -1])
            x_distance=choice([1,2,3,4,5])
            x_step=x_direction*x_distance
            
            y_direction=choice([1, -1])
            y_distance=choice([1,2,3,4,5])
            y_step=y_direction*y_distance
            self.x_values.append(self.x_values[-1]+x_step)
            self.y_values.append(self.y_values[-1]+y_step)
rw=randomwalk()
rw.fill_walk()
point_numbers=list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=3)
plt.scatter(0,0,c="green",s=5)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c="red",s=5)
plt.show()
