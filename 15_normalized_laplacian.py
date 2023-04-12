import cv2
import numpy

img = cv2.imread("resource/screenshot.png", cv2.IMREAD_COLOR)
cv2.imshow("img", img)

## blur-> gray -> laplacian
img_blur = cv2.medianBlur(img, 7)
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
img_lap = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=7)
#cv2.imshow("img_lap", img_lap)

## black edges
img_b_edge = 255 - img_lap
#cv2.imshow("img_b_edge", img_b_edge)

## normalizedInverseAlpha
normalizedInverseAlpha = img_b_edge/255
cv2.imshow("img_norm", normalizedInverseAlpha)

#print(img_norm[0:10, 0:10])

## Applying edge on the orginal image
channels = cv2.split(img)
for channel in channels:
    channel[:] = channel * normalizedInverseAlpha

img_color_lap = cv2.merge(channels)
cv2.imshow("img_color_lap", img_color_lap)


cv2.waitKey()
cv2.destroyAllWindows()

