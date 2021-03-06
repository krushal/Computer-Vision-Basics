

# import the necessary packages
import numpy as np
import cv2

# load the image and display it it
image = cv2.imread("split_rock.jpeg")
cv2.imshow("Original", image)

# Masking allows us to focus only on parts of an image that interest us.
# A mask is the same size as our image, but has only two pixel values,
# 0 and 255. Pixels with a value of 0 are ignored in the orignal image,
# and mask pixels with a value of 255 are allowed to be kept. For example,
# let's construct a rectangular mask that displays only the person in
# the image
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (200, 220), (350, 450), 255, -1)
cv2.imshow("Mask", mask)

# Apply out mask -- notice how only the person in the image is cropped out
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# Now, let's make a circular mask with a radius of 100 pixels and apply the
# mask again
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (270, 250), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)