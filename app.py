from flask import Flask, render_template, Response,request
import cv2
import face_recognition
import numpy as np   #library for masked arrays and matrices

app=Flask(__name__)
camera = cv2.VideoCapture(0)

# Uploading and encodings images.
first_image = face_recognition.load_image_file("images/Youssef.jpg")
first_encoding = face_recognition.face_encodings(first_image)[0]

second_image = face_recognition.load_image_file("images/Elon Musk.jpg")
second_encoding = face_recognition.face_encodings(second_image)[0]

third_image = face_recognition.load_image_file("images/Jeff Bezoz.jpg")
third_encoding = face_recognition.face_encodings(third_image)[0]


# Create arrays of encodings of known faces and their names
known_face_encodings = [
    first_encoding,
    second_encoding,
    third_encoding
]
known_face_names = [
    "Youssef",
    "Elon Musk",
    "Jeff bezoz"
]
# Inicialize variables
face_locations = []
face_encodings = []
#process_this_frame = True

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the frame of webcam
        if not success:
            break
        else:
            # reduce the video frame
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            # convert the image to rgb color
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
           
            # Face search on the frame
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            face_names = []
            for face_encoding in face_encodings:
                # check if the face matches the known face
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Desconocido"
                #face_names = []
                #  use the known face with the shortest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)
            
            # Display the results
            for (top, right, bottom, left),name in zip(face_locations, face_names):
                #Rescale the face locations back to origin size, since the frame we detected was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

               
                # Drwa the rectangle around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)
                  
                font = cv2.FONT_HERSHEY_SIMPLEX
                # write the of known face above on the rectangle
                cv2.putText(frame, name, (left + 4, top - 4), font, 1.5, (0, 0, 255), 4)
  
             # Convert the jpg images on bytes for execute in the browser
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# Initial page
@app.route('/')
def index():
    return render_template('index.html')

# Video transmission path
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# execute the App
if __name__ == '__main__':
    app.run(debug=True)