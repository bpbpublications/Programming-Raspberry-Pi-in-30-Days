#import libraries
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

#Define button
button = Button(17)

#Define Camera and resolution
camera = PiCamera()
camera.resolution = (1280, 720)

#Define moment for our timestamp
moment = datetime.now()

#Define a function for image capture
def capture():
    camera.capture('/home/pi/Pictures/test_%02d_%02d_%02d.mjpg' % (moment.hour, moment.minute, moment.second))

#Capture image when pressing button
button.when_pressed = capture

#Keep the code running
pause()

