import cv2
import face_recognition        # import the face recognition library
img = cv2.imread("Messi1.webp")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)     #convert the image bgr to rgb colour 

# this function returns the face encoding of 128 dimensions for each face of the image
img_encoding = face_recognition.face_encodings(rgb_img)[0]  

img2 = cv2.imread("images/Messi.webp")                     
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)                   
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

#Compares one list of face encodings with another to see if they match, returning True or False
result = face_recognition.compare_faces([img_encoding], img_encoding2) 
print("Result: ", result)
cv2.waitKey(0)