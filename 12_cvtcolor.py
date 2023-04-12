import cv2
import numpy

img = cv2.imread("resource/screenshot.png", cv2.IMREAD_UNCHANGED)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("img", img)
cv2.imshow("img_gray", img_gray)

img_back = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
cv2.imshow("img_back_color", img_back)


cv2.waitKey()
