import cv2
import numpy as np

img = cv2.imread("resource/sudoku.png")
## Color Space Conversions 
## https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,120)

minLineLength = 20
maxLineGap = 5
threshold = 100 #The minimum number of intersecting points to detect a line

lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold, minLineLength,maxLineGap)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
                                             

cv2.imshow("edges", edges)
cv2.imshow("lines", img)
cv2.waitKey()
cv2.destroyAllWindows()

