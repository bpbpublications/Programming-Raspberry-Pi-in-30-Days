#Import libraries
from guizero import App, Text, Slider
from gpiozero import AngularServo

# Define the servo
angular_servo = AngularServo(17, min_angle=-90, max_angle=90)

#Define a function to change the angle of the servo
def servo_angle(slider_value):
    angular_servo.angle = int(slider_value)
    
# Define the app with the title hello world
app = App(title="Angular Servo Control")
# Add color to our app
app.bg = "#41f1e6"
# Add a message to the app
message =Text(app, text="Move The Slider To Change the Angle")
# Add a slider to the app
slider_sample = Slider(app, start=-90, end=90, command=servo_angle)
# Add color to our slider
slider_sample.bg = "#f141e1"
# Display the app
app.display()