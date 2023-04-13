import cv2
import numpy

### More for this
### https://docs.opencv.org/4.x/d1/d32/tutorial_py_contour_properties.html
###

img = cv2.imread("resource/sparta.png", cv2.IMREAD_COLOR)
cv2.imshow("img_org", img)

##
ret, thresh = cv2.threshold( cv2.cvtColor(img.copy(), 
                             cv2.COLOR_BGR2GRAY), 128, 255, cv2.THRESH_BINARY)  

print(ret)

'''
Contour Approximation Method
 cv2.CHAIN_APPROX_SIMPLE
 cv2.CHAIN_APPROX_NONE
'''
contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

'''
https://docs.opencv.org/4.x/d9/d8b/tutorial_py_contours_hierarchy.html
Hierarchy Representation in OpenCV
[Next, Previous, First_Child, Parent]
'''
#print(hier)

for c in contours:
    #print(c.shape) #(point_size, 1, 2) why 2?

    ## Bounding Rectangle: Straight Bounding Rectangle
    x,y,w,h = cv2.boundingRect(c)
    #print(x,y,w,h)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    ## Bounding Rectangle: Rotated Rectangle
    rect = cv2.minAreaRect(c) #rect: ( center (x,y), (width, height), angle of rotation )
    box = cv2.boxPoints(rect)
    box = numpy.int0(box)
    cv2.drawContours(img,[box],0,(0,0,255),2)

    ## Minimum Enclosing Circle
    (x,y),radius = cv2.minEnclosingCircle(c)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(img,center,radius,(0,255,0),2)


    ## Fitting an Ellipse 
    ellipse = cv2.fitEllipse(c)
    cv2.ellipse(img,ellipse,(0,200,200),2)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img) 

cv2.waitKey()
cv2.destroyAllWindows()
                             
