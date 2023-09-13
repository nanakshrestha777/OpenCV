import cv2 as cv
import face_recognition

image = face_recognition.api.load_image_file('D:\My_study\Opencv\Face_recognition\download.jpg')
face_location = face_recognition.api.face_locations(image)

for (top,right,left,bottom) in face_location:
    cv.rectangle(image,(left,top),(right,bottom),(0,255,0),2)

cv.imshow('image',image)
cv.waitKey(0)
cv.destroyAllWindows()


video = cv.VideoCapture(0)
while True:
    ret, frame = video.read()

    rgb_frame = frame[:,:,::-1]

    face_location = face_recognition.api.face_locations(rgb_frame)

    face_landmarks = face_recognition.api.face_landmarks(rgb_frame,face_location)

    for landmarks in face_landmarks: #iterates over the elements in the face-landmarks list.
        for facial_feature in landmarks.keys(): #iterates over the keys of the current landmarks dictionary
            for landmark in landmarks[facial_feature]: #iterates over the list of coordinate tuples with a specific facial feature analysis on each individual landmark coordinate.
                cv.circle(frame,landmark,2,(0,255,0),-1) 
    
    cv.imshow('video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv.destroyAllWindows()


