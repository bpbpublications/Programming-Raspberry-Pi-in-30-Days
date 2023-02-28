#import libraries
from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from signal import pause

#define sensor and camera
pir = MotionSensor(17)
camera = PiCamera()
camera.resolution = (1280, 720)

#Define our timestamp
moment = datetime.now()

#Take a picture when there is change in infrared
pir.wait_for_motion()
camera.capture("/home/pi/Pictures/intruder_%02d_%02d_%02d.jpg" % (moment.hour, moment.minute, moment.second))

#Keep the code running
pause()
