#import libraries
from gpiozero import Button
from signal import pause

#define the button
button = Button(17)

#define a function 
def hello():
    print("Hello world")

#Attach the function to the button
button.when_pressed = hello

#Run the code indefinitely
pause()
