#import libraries
from guizero import App, PushButton, Text
from gpiozero import Servo

#Define the Servo
servo = Servo(17)

#Define our functions

def servomin():
    servo.min()

def servomid():
    servo.mid()

def servomax():
    servo.max()

#Define the app
app = App(title="Servo Control")
app.bg = "#41f1f1"

#Add some text
message = Text(app, text="Servo Buttons")
message.text_size = 20

#Define the buttons
button_min = PushButton(app, text="Min", command=servomin)
button_min.bg = "Green"
button_min.text_size = 20
button_mid = PushButton(app, text="Mid", command=servomid)
button_mid.bg = "Yellow"
button_mid.text_size = 20
button_max = PushButton(app, text="Max", command=servomax)
button_max.bg = "Orange"
button_max.text_size = 20

#display app
app.display()