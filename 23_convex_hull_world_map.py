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

contours, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = [] 
# calculate points for each contour
for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))

#print(hull)
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    #cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hier)
    # draw ith convex hull object
    print(hull.shape)
    cv2.drawContours(drawing, hull, i, color, 1, 8)

cv2.imshow("cnt", drawing)

cv2.waitKey()
cv2.destroyAllWindows()



