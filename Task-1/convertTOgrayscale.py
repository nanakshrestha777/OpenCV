import cv2

#Use openCV to read an image file path, convert it to grayscale and show it.


#Grayscaling is the process of converting an image from other color spaces
# e.g RGB, CMYK, HSV etc to shades of gray.

# Method 1 Using the cv2.cvtColor() function
image = cv2.imread('D:\My_study\Opencv\images.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)

# using cvtColor() function to grayscale the image

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)

cv2.waitKey(0)

cv2.destroyAllWindows()