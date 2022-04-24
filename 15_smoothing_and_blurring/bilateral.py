# import the necessary packages
import cv2

# load the image, display it, and construct the list of bilateral
# filtering parameters that we are going to explore
image = cv2.imread('split_rock.jpeg')
cv2.imshow("Original", image)
params = [(25, 41, 21), (25, 61, 39), (25, 81, 59)]

# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
	# apply bilateral filtering and display the image
	blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
	title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
	cv2.imshow(title, blurred)
	cv2.waitKey(0)