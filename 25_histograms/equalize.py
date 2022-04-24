
# import the necessary packages
import cv2

# load the image and convert it to grayscale
image = cv2.imread("beach.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization to stretch the constrast of our image
eq = cv2.equalizeHist(image)

# show our images -- notice how the constrast of the second image has
# been stretched
cv2.imshow("Original", image)
cv2.imshow("Histogram Equalization", eq)
cv2.waitKey(0)