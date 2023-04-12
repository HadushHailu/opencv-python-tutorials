import cv2
import numpy

img = cv2.imread("resource/screenshot.png", cv2.IMREAD_COLOR)
cv2.imshow("img", img)

## Directly from Color
img_lap = cv2.Laplacian(img, cv2.CV_8U, ksize = 7)
cv2.imshow("img_lap", img_lap)

## From grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_g_lap = cv2.Laplacian(img_gray, cv2.CV_8U, ksize = 7)
cv2.imshow("img_g_lap", img_g_lap)

## From blurred img
img_blur = cv2.medianBlur(img, 11)
img_b_lap = cv2.Laplacian(img_blur, cv2.CV_8U, ksize = 7)
cv2.imshow("img_blur_lap", img_b_lap)

## From blurred img
img_blur = cv2.medianBlur(img, 11)
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
img_bg_lap = cv2.Laplacian(img_gray, cv2.CV_8U, ksize = 7)
cv2.imshow("img_blur_gray_lap", img_bg_lap)

cv2.waitKey()
cv2.destroyAllWindows()


