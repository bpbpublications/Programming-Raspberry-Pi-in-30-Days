#import libraries
from time import sleep
from picamera import PiCamera

#Define our camera
camera = PiCamera()

#Set the resolution to whatever you want
camera.resolution = (1280, 720)

#Preview the camera 
camera.start_preview()

#Wait for a few seconds
sleep(3)

#Output to a file
camera.capture("first-picture.jpg")