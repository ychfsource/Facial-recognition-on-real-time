import cv2 as cv   # import the opencv library

img = cv.imread("images\Elon Musk.jpg")  # imread function to read the image by indicating its route

def rescaleFrame(frame, scale=.35):      # function to rescale the frame 
 width = int(frame.shape[1] * scale)     
 height = int(frame.shape[0] * scale)  

 dimension = (width,height)

 return cv.resize(frame, dimension, interpolation=cv.INTER_AREA) #function for image resizing

resized_image = rescaleFrame(img)   
cv.imshow('imagen', resized_image) 

captura = cv.VideoCapture(0)         
while True:                          
    isTrue, frame = captura.read()       
    cv.imshow('CapturaVideo', frame)       
    if cv.waitKey(20) & 0xFF == ord('d'):  
     break

captura.release()                  # release blockage
cv.destroyAllWindows()             # destroys all vetanas that have been created