#import libraries
from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from signal import pause

#define sensor and camera
pir = MotionSensor(17)
camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 25

#Define our timestamp
moment = datetime.now()

#Record video when there is change in infrared
pir.when_motion = camera.start_recording("/home/pi/Videos/intruder_%02d_%02d_%02d.h264" % (moment.hour, moment.minute, moment.second))
pir.when_no_motion = camera.stop_recording()
#Keep the code running
pause()
