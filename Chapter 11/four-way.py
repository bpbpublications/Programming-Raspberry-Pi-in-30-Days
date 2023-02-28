#import libraries
from guizero import App, Text, PushButton
from gpiozero import Robot

#Define our robot
robot = Robot(left=(13, 21), right=(17, 27))

# Define the functions for the buttons
def forward():
    robot.forward()

def backward():
    robot.backward()

def left():
    robot.left()

def right():
    robot.right()

def stop():
    robot.stop()

# Define the app
app = App(title="Robot Control")
# Add background color to the app
app.bg = "#41f18e"
# Define the text and text size
message = Text(app, text="Four Way Buttons")
message.text_size = 20
# Define the buttons and their functions and give them color
button1 = PushButton(app, text="^", align ="top")
button1.when_left_button_pressed = forward
button1.when_left_button_released = stop
button1.bg = "aqua"
button1.text_size = 20
button2 = PushButton(app, text="v", align ="bottom")
button2.when_left_button_pressed = backward
button2.when_left_button_released = stop
button2.bg = "aqua"
button2.text_size = 20
button3 = PushButton(app, text="<", align ="left")
button3.when_left_button_pressed = left
button3.when_left_button_released = stop
button3.bg = "aqua"
button3.text_size = 20
button4 = PushButton(app, text=">", align ="right")
button4.when_left_button_pressed = right
button4.when_left_button_released = stop
button4.bg = "aqua"
button4.text_size = 20

#Display the app
app.display()