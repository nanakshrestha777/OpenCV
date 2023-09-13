# Use openCV to read a video file path, converting each frame to grayscale and show it

import cv2 as cv

cap = cv.VideoCapture(r"./10 SECONDS VIDEO CLIP.mp4")

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Live', gray)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

    
