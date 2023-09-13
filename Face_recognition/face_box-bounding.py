import cv2 as cv
import face_recognition

# Load the image with faces
image_path = 'path_to_your_image.jpg'
image = face_recognition.api.load_image_file("D:\My_study\Opencv\Face_recognition\images.jpg")

# Detect faces in the loaded image
face_locations = face_recognition.api.face_locations(image)

# Draw bounding boxes around the detected faces in the image
for (top, right, bottom, left) in face_locations:
    # Draw a rectangle around the face using OpenCV
    cv.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)



# Display the image with bounding boxes
cv.imshow('Image', image)
cv.waitKey(0)
cv.destroyAllWindows()

live_cap = cv.VideoCapture(0)

while True:
    ret, frame  = live_cap.read()

    rgb_frame = frame[:,:,::-1]

    face_locations = face_recognition.api.face_locations(rgb_frame)

    for (top,right,bottom,left) in face_locations:
        cv.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)

    cv.imshow('Live',frame)
    if cv.waitKey(1) & 0xff == ord('q'):
        break
live_cap.release()
cv.destroyAllWindows


