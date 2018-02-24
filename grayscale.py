import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from copy import deepcopy
from PIL import Image

def rgb2gray(rgb):
    gray = (rgb[0]+rgb[1]+rgb[2])/3
    return [gray, gray, gray]

def reverseColor(rgb):
    return [255-rgb[0],255-rgb[1],255-rgb[2]]

img = Image.open('8bit.png')
img = numpy.asarray(img)

# copy list not reference
gray = deepcopy(img)
rev  = deepcopy(img)

for i in range(len(img)):
    for j in range(len(img[i])):
        color = gray[i][j]
        color = rgb2gray(color)
        gray[i][j] = color
        color = reverseColor(color)
        rev[i][j] = color

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(gray)
plt.subplot(2, 2, 3)
plt.imshow(rev)

plt.show()
