import cv2 as cv

# the haarcascade is a class for detecting objects in a video stream
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') 
    
cap = cv.VideoCapture(0)   #capture the video of camera
  
while True:  
    _, img = cap.read()   # reading the frame
   
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   # convert the image to gray scale
  
   # face detection
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  
  
    # Draw th erectangle around the face 
    for (x, y, w, h) in faces:  
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  
  
    cv.imshow('Video', img)  
  
    # exit if 'esc' key is pressed
    k = cv.waitKey(30) & 0xff  
    if k==27:  
        break  
          
cap.release()  
cv.waitKey(20)