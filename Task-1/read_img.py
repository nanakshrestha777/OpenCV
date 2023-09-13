import cv2
# Use openCV to read an image path and show it


image =cv2.imread('D:\My_study\Opencv\images.jpg')
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()