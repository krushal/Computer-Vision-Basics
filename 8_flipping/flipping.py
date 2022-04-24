
# import the necessary packages
import argparse
import cv2

# load the image and show it
image = cv2.imread('split_rock.jpeg')
cv2.imshow("Original", image)

# flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)