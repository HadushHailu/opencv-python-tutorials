# Display image in a window

import cv2
import numpy 

img = cv2.imread('resource/spot.png')
cv2.imshow('SPOT ROBOT', img)
cv2.waitKey() #wait forever
cv2.destroyAllWindows() #Destroy all opencv windows
