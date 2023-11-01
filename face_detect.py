import cv2
from random import randrange

#Pretrained data from haar cascade git
trained_face_detect_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#Image you want to detect the face of (code below for if you wanted to track an image)
#image = cv2.imread('many_faces.jpg')

#Capture video from webcam
#Can also instead of 0, make a video file that will track the faces in that (0 just makes it your webcam)
camera = cv2.VideoCapture(0)

#Loop forever over the frames until killed
while True:

    frame_read, frame = camera.read()


    #Convert image to grayscale, can use that if preferred
    grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect the face
    face_coords = trained_face_detect_data.detectMultiScale(grayscaled_image)

    #Loop through all the faces and draw rectangles around all of them
    #rectange(image, top left of the rectangle, bottom right of the rectangle, BGR of the rectangle, thickness of rectangle)
    for (x, y, w, h) in face_coords:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 3)

    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)

    ###Stop if space is pressed
    if key==32:
        break
    

'''
Code for if you were to just track an image
#Detect the face
face_coords = trained_face_detect_data.detectMultiScale(grayscaled_image)

#Loop through all the faces and draw rectangles around all of them
#rectange(image, top left of the rectangle, bottom right of the rectangle, BGR of the rectangle, thickness of rectangle)
for (x, y, w, h) in face_coords:
    cv2.rectangle(image, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 3)

#Display the image with faces (rectangle(s) will be black if grayscaled)
cv2.imshow('Christ Evans Yay', image)
cv2.waitKey()
'''





