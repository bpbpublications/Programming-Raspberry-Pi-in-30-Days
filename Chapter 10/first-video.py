#import libraries
from picamera import PiCamera
from time import sleep

#Define the camera
camera = PiCamera()

#Define a resolution and framerate
camera.resolution = (1280, 720)
camera.framerate = 25

#Start recording
camera.start_recording('/home/pi/Videos/test.h264')

#Record for 5 seconds
sleep(5)

#Stop recording
camera.stop_recording()