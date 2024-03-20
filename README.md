# Face-Detector
This app is able to take any video or image, and highlights all the faces in them in a rectangle. For this app, I used the opencv Python library, as well as a pre-trained haar cascade face detector model, which is attached in the files list. The program allows for any image or video that is saved in the environment to be assigned to static variables, and applies the fce detectors on them, producing a list of the coordinates of each face on the screen. We then use those coordinates to create a rectangle around each of those faces. For videos, we continue to loop through this entire process while the video successfully reads frames. This means that for the conversion of image to video, we just treat the video as a bunch of images that we are detecting the faces of each frame, and continue to loop through that until the video no longer reads any frames (the video ends). The detector can run until the video ends, or until the space bar is pressed.



