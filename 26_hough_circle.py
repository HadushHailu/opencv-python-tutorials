import cv2
import numpy as np

img = cv2.imread("resource/planets_black_sky.png")
## Color Space Conversions 
## https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)

#cany = cv2.Canny(blur, 50, 200)
#cv2.imshow("thresh", cany)

planets = cv2.cvtColor(blur,cv2.COLOR_GRAY2BGR)

# HOUGH_GRADIENT, HOUGH_GRADIENT_ALT

circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,100,
                           param1=300,
                           param2=30,
                           minRadius=0,
                           maxRadius=300)

print("orginal:", circles)
around = np.around(circles)
print("around:", around)
circles = np.uint16(around)
print("uint16:", circles)

for i in circles[0,:]:
    print(i)
    # draw the outer circle
    cv2.circle(planets,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(planets,(i[0],i[1]),2,(0,0,255),3)

                                             
cv2.imshow("HoughCircles", planets)

cv2.imshow("lines", img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
