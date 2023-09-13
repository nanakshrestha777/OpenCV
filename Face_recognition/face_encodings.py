import face_recognition

image_path = ["D:\My_study\Opencv\Face_recognition\images.jpg","D:\My_study\Opencv\Face_recognition\download.jpg"]

face_encodings = []

for image in image_path:
    img = face_recognition.load_image_file(image)

    face_locations = face_recognition.face_locations(img)

    if len(face_locations) > 0:
        top, right , bottom, left = face_locations[0]

        face_image = image[top:bottom,left:right]

        face_encoding = face_recognition.face_encodings(face_image[0])

        face_encodings.append(face_encoding)
print(face_encodings)

