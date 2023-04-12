import cv2
import numpy

img = cv2.imread("resource/screenshot.png", cv2.IMREAD_COLOR)

img_mb = cv2.medianBlur(img, 13)

#img_b = cv2.blur(img, 5)

cv2.imshow("img", img)
cv2.imshow("img_medianBlur", img_mb)
#cv2.imshow("img_blur", img_b)

cv2.waitKey()
