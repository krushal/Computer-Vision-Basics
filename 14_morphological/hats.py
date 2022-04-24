
# import the necessary packages
import argparse
import cv2

# load the image and convert it to grayscale
image = cv2.imread('brain-scan.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# construct a rectangular kernel and apply a blackhat operation which
# enables us to find dark regions on a light background
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

# similarly, a tophat (also called a "whitehat") operation will enable
# us to find light regions on a dark background
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# show the output images
cv2.imshow("Original", image)
cv2.imshow("Blackhat", blackhat)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)