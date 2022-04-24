
# import the necessary packages
import cv2

# load the image and show it
image = cv2.imread("split_rock.jpeg")
cv2.imshow("Original", image)

# cropping an image is accomplished using simple NumPy array slices --
# let's crop the face from the image
moon = image[150:350, 170:350]
cv2.imshow("Moon", moon)
cv2.waitKey(0)

# ...and now let's crop the entire body
light_house = image[250:500, 200:350]
cv2.imshow("Light house", light_house)
cv2.waitKey(0)