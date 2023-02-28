#import libraries
from picamera import PiCamera
from time import sleep
from datetime import datetime

#Define the camera
camera = PiCamera()

#Define a resolution and framerate
camera.resolution = (1280, 720)
camera.framerate = 25

#Define a moment here for the datetime
moment = datetime.now()

#Start recording and save the timestamp
camera.start_recording('test_%02d_%02d_%02d.h264'% (moment.hour, moment.minute, moment.second))

#Record for 5 seconds
sleep(5)

#Stop recording
camera.stop_recording()