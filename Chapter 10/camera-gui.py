#import libraries
from guizero import App, Text, PushButton
from picamera import PiCamera
from datetime import datetime

#Define the camera and resolution
camera = PiCamera()
camera.resolution = (1280, 720)

#Define the moment for our timestamp
moment = datetime.now()

#Define our function for picture capture
def picture_capture():
    camera.capture("/home/pi/Pictures/test_%02d_%02d_%02d.jpg" %  (moment.hour, moment.minute, moment.second))

#define app
app = App(title="Camera App")
app.bg = "aqua"

#Define text
message = Text(app, text="Say Cheese!")
message.text_size = 20

#Define the button
camera_button = PushButton(app, text="Click", command=picture_capture)
camera_button.bg = "red"
camera_button.text_size = 20

#Run the app
app.display()