
# import the necessary packages
import argparse
import imutils
import cv2

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread("teacup.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# apply Canny edge detection using a wide threshold, tight
# threshold, and automatically determined threshold
wide = cv2.Canny(blurred, 10, 200)
tight = cv2.Canny(blurred, 225, 250)
auto = imutils.auto_canny(blurred)

# show the images
cv2.imshow("Original", image)
cv2.imshow("Wide", wide)
cv2.imshow("Tight", tight)
cv2.imshow("Auto", auto)
cv2.waitKey(0)