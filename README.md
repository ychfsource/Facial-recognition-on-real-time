# Facial-recognition-on-real-time

Facial recognition is a way of identifying or confirming a person's identity through their face. Facial recognition systems can be used to identify people in photos, videos or in real time.


I have used python language to create the system and other libraires , this is the link for download python : https://www.python.org/downloads ,I have installed version 3.10

The libraries we must intall are these: opencv, Dlib, feca_recogniton, cmake, flask, caer


# Guide of libraries installation:

#  opencv:
#C:\>pip install opencv-contrib-python

#C:\>python -c "import cv2; print(cv2.__version__)"

4.5.5


#  dlib:
#C:\>pip install cmake

#C:\>pip install dlib

#  face_recogniton:
#C:\>pip install face_recognition

#  Flask:
#C:\>pip install flask:

You can use command "pip list" to list installed packages,including editables.
# Estructure

#I've created three files to check if the libraries are working:

test1.py, test2.py, test3.py

#test1.py: We will create a Python script called 'test1.py' to open the image and also for a video from our webcam.

#test2.py: we will create a file called 'test2.py' to compare images returning a true result if the images match and false if they do not.

#test3.py: In this last one we will create a programme to detect faces by means of a real-time video. 
 
Finally I've created app.py file whose we can display a webcam on real time into navegtor.
