# Example of HPF

import cv2
import numpy as np
from scipy import ndimage

'''
    Kernel is another array, that is usually smaller than the source image, and defines the 
    filtering action. A kernel could be a high pass, low pass(All 1), 
    or a custom that can detect certain features in the image.
'''

kernel_3x3 = np.array([[-1,-1,-1],
                       [-1,8,-1],
                       [-1,-1,-1]])

kernel_5x5 = np.array([[-1,-1,-1,-1,-1],
                       [-1, 1, 2, 1,-1],
                       [-1, 2, 4, 2,-1],
                       [-1, 1, 2, 1,-1],
                       [-1,-1,-1,-1,-1]])


img = cv2.imread("resource/screenshot.png", cv2.IMREAD_GRAYSCALE)

'''
cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType=BORDER_DEFAULT]]] )

    src: input image
    dst: output image
    ksize: Gaussian Kernel Size. [height width]. height and width should be odd and can 
            have different values. If ksize is set to [0 0], then ksize is computed from sigma values.
    sigmaX: Kernel standard deviation along X-axis (horizontal direction).
    sigmaY:	Kernel standard deviation along Y-axis (vertical direction). 
            If sigmaY=0, then sigmaX value is taken for sigmaY
    borderType: Specifies image boundaries while kernel is applied on image borders. 
                Possible values are : 
                    cv.BORDER_CONSTANT 
                    cv.BORDER_REPLICATE 
                    cv.BORDER_REFLECT 
                    cv.BORDER_WRAP 
                    cv.BORDER_REFLECT_101 
                    cv.BORDER_TRANSPARENT 
                    cv.BORDER_REFLECT101 
                    cv.BORDER_DEFAULT 
                    cv.BORDER_ISOLATED
'''

# LPF (Low pass filter)
# low pass filter (LPF) will smoothen the pixel if the difference with the surrounding
# pixels is lower than a certain threshold. This is used in denoising and blurring

blurred = cv2.GaussianBlur(img, (11,11), 0)

# Pixel value: 0 black, 255 white and -1 white and so on
g_hpf = img - blurred
my_hpf = blurred - img

'''
    we want to "convolve" an image with a
    given kernel and NumPy happens to only accept one-dimensional arrays.
    This does not mean that the convolution of deep arrays can't be achieved with
    NumPy, just that it would be a bit complex. Instead, ndimage (which is a part of
    SciPy)
'''
## HPF (High pass filters) - 
# boosts the intensity of a pixel, given its difference with its neighbors

k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

cv2.imshow("image", img)
cv2.imshow("image_k3", k3)
cv2.imshow("image_k5", k5)
#cv2.imshow("image_blurred", blurred)
cv2.imshow("image_ghpf", g_hpf)
#cv2.imshow("my_ghpf", my_hpf)

cv2.waitKey()
cv2.destroyAllWindows()


