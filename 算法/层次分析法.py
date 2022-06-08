
import numpy as np

mat = np.array([[1, 2, 3, 5],
                [0.5, 1, 3,4],
                [1/3, 1/3, 1,3],
                [1/5,1/4,1/3,1]])

eigenvalue, featurevector = np.linalg.eig(mat)

a=max(eigenvalue)
CR=(a-4)/(3*0.89)
print(CR)
mat=mat.T
print(mat)
list=[]
for i in range(4):
    a=sum(mat(i))
    list.append(a)