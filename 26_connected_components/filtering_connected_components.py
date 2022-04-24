# import the necessary packages
import numpy as np
import cv2

# load the input image from disk, convert it to grayscale, and
# threshold it
image = cv2.imread("license_plate.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

connectivity = 4
# apply connected component analysis to the thresholded image
output = cv2.connectedComponentsWithStats(
	thresh, connectivity, cv2.CV_32S)
(numLabels, labels, stats, centroids) = output
# initialize an output mask to store all characters parsed from
# the license plate
mask = np.zeros(gray.shape, dtype="uint8")

# loop over the number of unique connected component labels, skipping
# over the first label (as label zero is the background)
for i in range(1, numLabels):
	# extract the connected component statistics for the current
	# label
	x = stats[i, cv2.CC_STAT_LEFT]
	y = stats[i, cv2.CC_STAT_TOP]
	w = stats[i, cv2.CC_STAT_WIDTH]
	h = stats[i, cv2.CC_STAT_HEIGHT]
	area = stats[i, cv2.CC_STAT_AREA]
	# ensure the width, height, and area are all neither too small
	# nor too big
	keepWidth = w > 5 and w < 50
	keepHeight = h > 45 and h < 65
	keepArea = area > 500 and area < 1500
	# ensure the connected component we are examining passes all
	# three tests
	if all((keepWidth, keepHeight, keepArea)):
		# construct a mask for the current connected component and
		# then take the bitwise OR with the mask
		print("[INFO] keeping connected component '{}'".format(i))
		componentMask = (labels == i).astype("uint8") * 255
		mask = cv2.bitwise_or(mask, componentMask)
	
# show the original input image and the mask for the license plate
# characters
cv2.imshow("Image", image)
cv2.imshow("Characters", mask)
cv2.waitKey(0)