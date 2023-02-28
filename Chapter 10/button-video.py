#import libraries
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

#Define buttons
button_record = Button(17)
button_stop = Button(27)

#Define Camera, resolution and framerate
camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 25

#Define moment for our timestamp
moment = datetime.now()

#Define a function for video capture
def capture():
    camera.start_recording('/home/pi/Videos/video_%02d_%02d_%02d.mjpg' % (moment.hour, moment.minute, moment.second))

def stop_recording():
    camera.stop_recording()

#Capture video and stop recording when done
button_record.when_pressed = capture
button_stop.when_pressed = stop_recording

#Keep the code running
pause()