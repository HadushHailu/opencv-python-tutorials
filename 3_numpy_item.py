import cv2
import numpy

img = cv2.imread("RandomColor.png")

#IMREAD_ANYCOLOR = 4
#IMREAD_ANYDEPTH = 2
#IMREAD_COLOR = 1
#IMREAD_GRAYSCALE = 0
#IMREAD_LOAD_GDAL = 8
#IMREAD_UNCHANGED = -1

print(img.shape)
print(img.item(99,120,0))

img.itemset((99,129,0), 0)
print(img.item(99,129,0))


img[:, :, 1] = 0
print(img.shape)
cv2.imwrite("NoGreen.png", img)
