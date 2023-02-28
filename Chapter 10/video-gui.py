#import libraries
from guizero import App, Text, PushButton
#from picamera import PiCamera
from datetime import datetime

#Define the camera and resolution
camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 25

#Define the moment for our timestamp
moment = datetime.now()

#Define our functions to record and stop recording

def record_video():
    camera.start_recording('/home/pi/Videos/test_%02d_%02d_%02d.h264'% (moment.hour, moment.minute, moment.second))

def stop_record():
    camera.stop_recording()

#Define the app
app = App(title="Video GUI")
app.bg = "aqua"

#Add text
message = Text(app, text="Press to Record")
message.text_size = 20

#Add push buttons
record_button = PushButton(app, text="Record", command=record_video)
record_button.bg = "green"
record_button.text_size = 20
stop_button = PushButton(app, text="Stop", command=stop_record)
stop_button.bg = "red"
stop_button.text_size = 20

#Display the app
app.display()

