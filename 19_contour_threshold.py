import cv2
import numpy as np
'''
https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
Contours can be explained simply as a curve joining all the continuous points (along the boundary), 
having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.

    For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
    Since OpenCV 3.2, findContours() no longer modifies the source image.
    In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

'''

## 
img = cv2.imread("resource/sink2.png", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#img = img[700:1200, 700:1500]

'''
    cv.THRESH_BINARY
    cv.THRESH_BINARY_INV
    cv.THRESH_TRUNC
    cv.THRESH_TOZERO
    cv.THRESH_TOZERO_INV
'''
## https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY) 

cv2.imshow("threshold", thresh)

##
'''
    cv2.RETR_EXTERNAL
    cv2.RETR_LIST
    cv2.RETR_CCOMP
    cv2.RETR_TREE
'''
## https://docs.opencv.org/3.4/d9/d8b/tutorial_py_contours_hierarchy.html

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(hierarchy)

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

## img, contour, contourIdx -1(all), marker color, marker thickness
img = cv2.drawContours(color, contours, -1, (0,0,255), 4)

cv2.imshow("contours", img)

cv2.waitKey()
cv2.destroyAllWindows()
