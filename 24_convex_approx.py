### A convex shape is one where there are two points
### within this shape whose connecting line goes outside the perimeter of the shape itself.

## https://learnopencv.com/convex-hull-using-opencv-in-python-and-c/

import cv2
import numpy as np


src = cv2.imread("resource/world_map.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src.copy(), cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3, 3)) # blur the image
cv2.imshow("gray", gray)
cv2.imshow("blur", blur)

ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)

## contours: tuple of (pts, 1, 2), (pts, 1, 2), (pts, 1, 2)
contours, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

##
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)


for cnt in contours:
    # creating convex hull object for each contours
    hull = cv2.convexHull(cnt, False)

    ## if hull: points, if [hull]: lines
    cv2.drawContours(drawing, [hull], -1, (0,0,255), 1)

    '''
    ## approximate bounding polygon
    The function cv::approxPolyDP approximates a curve or a polygon with another curve/polygon 
    with less vertices so that the distance between them is less or equal to the specified precision. 
    It uses the Douglas-Peucker algorithm http://en.wikipedia.org/wiki/Ramer-Douglas-Peucker_algorithm

    '''
   
    '''
    An epsilon value representing the maximum discrepancy between the
    original contour and the approximated polygon (the lower the value, the
    closer the approximated value will be to the original contour)
    '''
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.drawContours(drawing, [approx], -1, (0,255,0), 1)

cv2.imshow("drawing", drawing)
cv2.waitKey()
cv2.destroyAllWindows()



