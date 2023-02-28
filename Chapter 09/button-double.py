#import libraries
from gpiozero import Button
from signal import pause

#define the button
button = Button(17)

#define functions
def hello():
    print("Button pressed")

def goodbye():
    print("Button released")

#Attach functions to the button
button.when_pressed = hello
button.when_released = goodbye

#Run the code indefinitely
pause()