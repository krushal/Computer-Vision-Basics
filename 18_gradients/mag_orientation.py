
# import the necessary packages
import numpy as np
import cv2

lower_angle =90
upper_angle =91.0

# load the image, convert it to grayscale, and display the original
# image
image = cv2.imread("bricks.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# compute gradients along the X and Y axis, respectively
gX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

# compute the gradient magnitude and orientation, respectively
mag = np.sqrt((gX ** 2) + (gY ** 2))
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

# find all pixels that are within the upper and low angle boundaries
idxs = np.where(orientation >= lower_angle, orientation, -1)
idxs = np.where(orientation <= upper_angle, idxs, -1)
mask = np.zeros(gray.shape, dtype="uint8")
mask[idxs > -1] = 255

# show the images
cv2.imshow("Mask", mask)
cv2.waitKey(0)