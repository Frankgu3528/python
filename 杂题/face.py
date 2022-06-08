from PIL import Image
im1 = Image.open("C:\\yzy.jpg","r")
im2 = Image.open("C:\\face.jpg","r")
import numpy as np
im1 = np.array(im1)
im2 = np.array(im2)
print(im1.shape)
print(im2.shape)
#im1=im1[:800,:560]
print(im1.shape)
im=0.6*im1+0.4*im2
im=im.astype(np.uint8)
Image.fromarray(im).show()
