# Face-Detector
This is a program that can either use a photo, or video, and keep track of all the faces on the screen at once. It uses a pre-trained algorithm to detect a face (haar face detector), and based on this trained model, uses that to recognize any face on the screen. It does this by using the face classifier from haar cascade to constantly get the coordinates of the face(s) on the screen, and based on that, a rectangle is created around the face(s). The program runs indefinitely until a space bar is pressed. Can also work for any video, or photo, as long as it is in the VS environment, and it is assigned to the static variables image or video.
Credit to @Clever Programmer on Youtube


