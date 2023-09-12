import cv2 as cv
# Use openCV to capture live video feed and show it


cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
