import cv2
import numpy 

img = cv2.imread('spot.png')

my_roi = img[0:100, 0:100]

img[150:250, 150:250] = my_roi

print("shape", img.shape)
print("size", img.size)
print("datype", img.dtype)

cv2.imwrite('spot_indexed.png', img)


