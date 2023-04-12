import cv2
import numpy

img = cv2.imread("resource/screenshot.png", cv2.IMREAD_COLOR)
cv2.imshow("img", img)

## kernel
kernel = numpy.array([[-1, -1, -1],
                      [-1, 9, -1],
                      [-1, -1, -1]])


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_filt = cv2.filter2D(img_gray, -1, kernel)
cv2.imshow("img_filtered", img_filt)

cv2.waitKey()
cv2.destroyAllWindows()

