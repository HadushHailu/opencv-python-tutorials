import cv2
import numpy as np

## Use the OpenCV functions pyrUp() and pyrDown() to downsample or upsample a given image
## https://docs.opencv.org/3.4/d4/d1f/tutorial_pyramids.html
img_org = cv2.imread("resource/sparta.png", cv2.IMREAD_UNCHANGED)
print("Size of org_img: ", img_org.shape)
cv2.imshow("img_org", img_org)

img = cv2.pyrDown(img_org)
print("Size of img: ", img.shape)
cv2.imshow("img", img)

img1 = cv2.pyrDown(img)
print("Size of img1: ", img1.shape)
cv2.imshow("img1", img1)

ret, thresh = cv2.threshold( cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 
                             127, 255, cv2.THRESH_BINARY)

contours, hier = cv2.findContours(thresh,
                                  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # find bounding box coordinates
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    # find minimum area
    rect = cv2.minAreaRect(c)
    # calculate coordinates of the minimum area rectangle
    box = cv2.boxPoints(rect)
    # normalize coordinates to integers
    box = np.int0(box)
    # draw contours
    cv2.drawContours(img, [box], 0, (0,0, 255), 3)
    # calculate center and radius of minimum enclosing circle
    (x,y),radius = cv2.minEnclosingCircle(c)
    # cast to integers
    center = (int(x),int(y))
    radius = int(radius)
    # draw the circle
    img = cv2.circle(img,center,radius,(0,255,0),2)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img)
cv2.waitKey()
